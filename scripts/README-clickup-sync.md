# Sync docs to ClickUp

On every push to `main`, the workflow `.github/workflows/sync-clickup-docs.yml`
mirrors this repo's `docs/` and `decisions/` folders into one ClickUp Doc.

## What it builds

```
Main page  (intro — docs/README.md)
  |- Marketing            (docs/marketing/)
  |    `- Brand
  |- Metrics
  |    `- Framework
  |- Product
  |    |- PRD
  |    `- Roadmap
  |- Tech
  |    `- Architecture
  `- Decision             (decisions/)
       |- ADR
       |- Council
       `- PR-FAQ
```

Each folder becomes a page; a folder's `README.md` becomes that page's content,
and the other markdown files become child pages. Page names come from each file's
first `# heading`.

## One-time setup

### 1. Get a ClickUp personal API token
ClickUp → your avatar → **Settings** → **Apps** → **API Token** → **Generate**.
It starts with `pk_`. (Tokens never expire.)

### 2. Get your Workspace id
Open ClickUp in the browser. The number right after `app.clickup.com/` in the URL
is your Workspace (team) id — e.g. `https://app.clickup.com/9008123456/...` → `9008123456`.

### 3. (Recommended) Get a Doc id
Create an empty Doc in ClickUp where you want the docs to live, open it, and copy
the id from the URL (the part after `/dc/`). Giving the workflow a fixed Doc id is
the safest option — it always updates the same Doc.

If you skip this, the workflow finds a Doc by name (`CLICKUP_DOC_NAME`, default
"Product Documentation") or creates one, and prints the new id in the run log so
you can save it.

### 4. Add the values to GitHub
In the repo: **Settings → Secrets and variables → Actions**.

Add one **secret**:

| Secret | Value |
| --- | --- |
| `CLICKUP_TOKEN` | your `pk_...` token |

Add these **variables** (Variables tab):

| Variable | Value | Required |
| --- | --- | --- |
| `CLICKUP_WORKSPACE_ID` | your workspace id | yes |
| `CLICKUP_DOC_ID` | the Doc id from step 3 | recommended |
| `CLICKUP_DOC_NAME` | Doc name for find-or-create | optional |

## Run it

- **Automatic:** push a change under `docs/` or `decisions/` to `main`.
- **By hand:** repo → **Actions** → **Sync docs to ClickUp** → **Run workflow**.

## Test locally

```bash
# See the planned page tree — makes no API calls:
python3 scripts/sync_clickup_docs.py --dry-run

# Do a real sync from your machine:
export CLICKUP_TOKEN=pk_xxx
export CLICKUP_WORKSPACE_ID=9008123456
export CLICKUP_DOC_ID=abcd-1234        # optional but recommended
python3 scripts/sync_clickup_docs.py
```

The script uses only Python's standard library — no `pip install` needed.

## Good to know

- **Markdown** is sent to ClickUp in the `content` field with `content_format:
  "text/md"`, so headings, lists, tables, and code blocks come across.
- **Re-runs update, not duplicate.** Pages are matched by name inside their parent.
- **Renaming a file's `# heading`** changes the page name, so the sync will create a
  new page and leave the old one. Rename the old page in ClickUp (or delete it) if needed.
- **No auto-delete.** ClickUp's public API has no "delete page" endpoint, so removing
  a markdown file does **not** remove its ClickUp page. Delete it by hand in ClickUp.
- The Docs API needs a ClickUp plan that includes API access to Docs.
