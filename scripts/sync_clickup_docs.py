#!/usr/bin/env python3
"""
Sync the repo's docs/ and decisions/ folders into a single ClickUp Doc.

Structure created in ClickUp (mirror folders):

    Main page  (intro = docs/README.md)
      |- Marketing            (docs/marketing/ -> folder page)
      |    `- Brand           (docs/marketing/brand.md)
      |- Metrics
      |    `- Framework
      |- Product
      |    |- PRD
      |    `- Roadmap
      |- Tech
      |    `- Architecture
      `- Decision             (decisions/ -> container page)
           |- ADR             (decisions/adr/README.md + its records)
           |- Council
           `- PR-FAQ

Markdown is sent to ClickUp in the `content` field with `content_format: "text/md"`
(that is the ClickUp parameter that accepts Markdown). Pages are matched by name
inside their parent, so re-running only updates pages instead of duplicating them.

Only Python's standard library is used (no pip install needed).

Environment variables
  CLICKUP_TOKEN         (required)  Personal API token, starts with "pk_".
  CLICKUP_WORKSPACE_ID  (required)  Numeric Workspace (team) id.
  CLICKUP_DOC_ID        (optional, recommended)  Existing Doc id to sync into.
  CLICKUP_DOC_NAME      (optional)  Doc name used for find-or-create. Default "Product Documentation".
  CLICKUP_PARENT_ID     (optional)  Parent id used only when creating a new Doc. Defaults to the workspace id.
  CLICKUP_PARENT_TYPE   (optional)  Parent type for a new Doc: 4 Space, 5 Folder, 6 List, 7 Everything, 12 Workspace. Default 7.
  REPO_ROOT             (optional)  Repo root path. Default: parent of this script's folder.

Usage
  python3 scripts/sync_clickup_docs.py            # do the sync
  python3 scripts/sync_clickup_docs.py --dry-run  # print the planned tree, call nothing
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.clickup.com"
MD = "text/md"

# Folders in the repo we mirror. The first one is the "main page" (intro).
DOCS_DIR = "docs"
DECISIONS_DIR = "decisions"
DECISIONS_PAGE_NAME = "Decision"  # the user asked for a sub-level called "decision"


# --------------------------------------------------------------------------- #
# Tiny ClickUp API client (stdlib only)
# --------------------------------------------------------------------------- #
class ClickUp:
    def __init__(self, token, workspace_id):
        self.token = token
        self.workspace_id = str(workspace_id)

    def _request(self, method, path, query=None, body=None):
        url = BASE + path
        if query:
            url += "?" + urllib.parse.urlencode(query)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", self.token)
        req.add_header("Accept", "application/json")
        if data is not None:
            req.add_header("Content-Type", "application/json")

        for attempt in range(6):
            try:
                with urllib.request.urlopen(req) as resp:
                    raw = resp.read().decode("utf-8")
                    return json.loads(raw) if raw else {}
            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", "replace")
                # Back off and retry on rate limit / transient server errors.
                if e.code == 429 or 500 <= e.code < 600:
                    wait = int(e.headers.get("Retry-After", "0") or 0) or (2 ** attempt)
                    sys.stderr.write(f"  ! {e.code} on {method} {path}; retry in {wait}s\n")
                    time.sleep(wait)
                    continue
                raise SystemExit(f"ClickUp API error {e.code} on {method} {path}: {detail}")
            except urllib.error.URLError as e:
                wait = 2 ** attempt
                sys.stderr.write(f"  ! network error ({e.reason}); retry in {wait}s\n")
                time.sleep(wait)
        raise SystemExit(f"ClickUp API kept failing on {method} {path}")

    # Docs -----------------------------------------------------------------
    def search_docs(self):
        docs, cursor = [], None
        while True:
            q = {"limit": 100, "deleted": "false", "archived": "false"}
            if cursor:
                q["cursor"] = cursor
            res = self._request("GET", f"/api/v3/workspaces/{self.workspace_id}/docs", query=q)
            docs.extend(res.get("docs", []))
            cursor = res.get("next_cursor")
            if not cursor:
                return docs

    def create_doc(self, name, parent_id, parent_type):
        body = {
            "name": name,
            "visibility": "PRIVATE",
            "create_page": False,  # we create the intro page ourselves
            "parent": {"id": str(parent_id), "type": int(parent_type)},
        }
        return self._request("POST", f"/api/v3/workspaces/{self.workspace_id}/docs", body=body)

    def get_pages(self, doc_id):
        return self._request(
            "GET",
            f"/api/v3/workspaces/{self.workspace_id}/docs/{doc_id}/pages",
            query={"max_page_depth": -1, "content_format": MD},
        )

    def create_page(self, doc_id, name, content, parent_page_id=None):
        body = {"name": name, "content": content, "content_format": MD}
        if parent_page_id:
            body["parent_page_id"] = parent_page_id
        return self._request(
            "POST", f"/api/v3/workspaces/{self.workspace_id}/docs/{doc_id}/pages", body=body
        )

    def edit_page(self, doc_id, page_id, name, content):
        body = {
            "name": name,
            "content": content,
            "content_format": MD,
            "content_edit_mode": "replace",
        }
        return self._request(
            "PUT",
            f"/api/v3/workspaces/{self.workspace_id}/docs/{doc_id}/pages/{page_id}",
            body=body,
        )


# --------------------------------------------------------------------------- #
# Build the desired page tree from the repo
# --------------------------------------------------------------------------- #
def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_h1(md_text):
    """Return (title, body). If the file starts with an H1, use it as the title
    and drop that line from the body so ClickUp does not show the title twice."""
    lines = md_text.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].lstrip().startswith("# "):
        title = lines[i].lstrip()[2:].strip()
        body = "\n".join(lines[:i] + lines[i + 1:]).strip("\n")
        return title, body
    return None, md_text


def nice_name(folder):
    return folder.replace("-", " ").replace("_", " ").strip().title()


def node(key, name, content, children):
    return {"key": key, "name": name, "content": content or "", "children": children}


def build_folder_node(abs_dir, rel_dir, name_override=None):
    """Turn a directory into a page. A README.md becomes the page's content;
    other markdown files and sub-folders become child pages."""
    entries = sorted(os.listdir(abs_dir))
    readme = None
    for e in entries:
        if e.lower() == "readme.md":
            readme = e
            break

    if readme:
        title, body = split_h1(read_text(os.path.join(abs_dir, readme)))
        name = name_override or title or nice_name(os.path.basename(rel_dir))
        content = body
    else:
        name = name_override or nice_name(os.path.basename(rel_dir))
        content = ""  # filled in below with a small section note

    children = []
    subdirs = [e for e in entries if os.path.isdir(os.path.join(abs_dir, e))]
    files = [
        e for e in entries
        if e.lower().endswith(".md") and e.lower() != "readme.md"
        and os.path.isfile(os.path.join(abs_dir, e))
    ]

    for d in sorted(subdirs):
        children.append(build_folder_node(os.path.join(abs_dir, d), f"{rel_dir}/{d}"))
    for fn in sorted(files):
        title, body = split_h1(read_text(os.path.join(abs_dir, fn)))
        leaf_name = title or nice_name(os.path.splitext(fn)[0])
        children.append(node(f"{rel_dir}/{fn}", leaf_name, body, []))

    # If a folder page has no README content, add a small note so it is not blank.
    if not content:
        if children:
            listed = ", ".join(c["name"] for c in children)
            content = f"_This section groups the following pages: {listed}._"
        else:
            content = "_This section is empty._"

    return node(rel_dir, name, content, children)


def build_tree(repo_root):
    docs_abs = os.path.join(repo_root, DOCS_DIR)
    if not os.path.isdir(docs_abs):
        raise SystemExit(f"Could not find '{DOCS_DIR}/' in {repo_root}")

    # Main page = the docs/ folder (content from docs/README.md).
    root = build_folder_node(docs_abs, DOCS_DIR)

    # Attach decisions/ as the "Decision" sub-page, last.
    decisions_abs = os.path.join(repo_root, DECISIONS_DIR)
    if os.path.isdir(decisions_abs):
        decision = build_folder_node(decisions_abs, DECISIONS_DIR, name_override=DECISIONS_PAGE_NAME)
        root["children"].append(decision)

    return root


# --------------------------------------------------------------------------- #
# Sync the desired tree into ClickUp
# --------------------------------------------------------------------------- #
def flatten_existing(pages, parent_id=None, out=None):
    """Index existing ClickUp pages as {parent_page_id or '': {name: page}}."""
    if out is None:
        out = {}
    for p in pages:
        pid = p.get("parent_page_id") or ""
        out.setdefault(pid, {})[p.get("name", "")] = p
        if p.get("pages"):
            flatten_existing(p["pages"], p["id"], out)
    return out


def resolve_doc(cu):
    """Return a doc id, creating the doc if needed."""
    doc_id = os.environ.get("CLICKUP_DOC_ID", "").strip()
    if doc_id:
        print(f"Using existing Doc id: {doc_id}")
        return doc_id

    name = os.environ.get("CLICKUP_DOC_NAME", "Product Documentation").strip()
    for d in cu.search_docs():
        if d.get("name") == name and not d.get("deleted") and not d.get("archived"):
            print(f"Found existing Doc '{name}': {d['id']}")
            return d["id"]

    parent_id = os.environ.get("CLICKUP_PARENT_ID", "").strip() or cu.workspace_id
    parent_type = os.environ.get("CLICKUP_PARENT_TYPE", "7").strip() or "7"
    created = cu.create_doc(name, parent_id, parent_type)
    print(f"Created new Doc '{name}': {created['id']}")
    print(f">>> Save this as the CLICKUP_DOC_ID variable to reuse it next time: {created['id']}")
    return created["id"]


def sync_node(cu, doc_id, node_, parent_page_id, existing_index, indent=0):
    bucket = existing_index.get(parent_page_id or "", {})
    match = bucket.get(node_["name"])

    # Special case: an existing root page that ClickUp auto-made can be adopted
    # as the main page even if its name differs, so we don't create a duplicate.
    if match is None and parent_page_id is None:
        roots = existing_index.get("", {})
        if len(roots) == 1:
            match = next(iter(roots.values()))

    pad = "  " * indent
    if match:
        page_id = match["id"]
        old = (match.get("content") or "").strip()
        new = node_["content"].strip()
        if old == new and match.get("name") == node_["name"]:
            print(f"{pad}= {node_['name']} (unchanged)")
        else:
            cu.edit_page(doc_id, page_id, node_["name"], node_["content"])
            print(f"{pad}~ {node_['name']} (updated)")
    else:
        created = cu.create_page(doc_id, node_["name"], node_["content"], parent_page_id)
        page_id = created["id"]
        print(f"{pad}+ {node_['name']} (created)")

    for child in node_["children"]:
        sync_node(cu, doc_id, child, page_id, existing_index, indent + 1)


def print_tree(node_, indent=0):
    print("  " * indent + "- " + node_["name"])
    for c in node_["children"]:
        print_tree(c, indent + 1)


def main():
    dry_run = "--dry-run" in sys.argv
    repo_root = os.environ.get("REPO_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    tree = build_tree(repo_root)

    if dry_run:
        print("DRY RUN — planned ClickUp page tree:\n")
        print_tree(tree)
        print("\n(no API calls made)")
        return

    token = os.environ.get("CLICKUP_TOKEN", "").strip()
    workspace_id = os.environ.get("CLICKUP_WORKSPACE_ID", "").strip()
    if not token or not workspace_id:
        raise SystemExit("CLICKUP_TOKEN and CLICKUP_WORKSPACE_ID must be set.")

    cu = ClickUp(token, workspace_id)
    doc_id = resolve_doc(cu)

    existing_index = flatten_existing(cu.get_pages(doc_id))
    print("\nSyncing pages:")
    sync_node(cu, doc_id, tree, None, existing_index)
    print("\nDone.")


if __name__ == "__main__":
    main()
