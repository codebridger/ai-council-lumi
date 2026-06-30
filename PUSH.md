# First push — one command

This template was built outside your machine, so it has no git history yet and is not on GitHub. Run the command below **on your own machine** (where the GitHub CLI `gh` is logged in) to create the repo and push.

> You can delete this file after the first push — it is only setup notes.

## 1. Check gh is logged in

```bash
gh auth status
```

If it is not logged in, run `gh auth login` first.

## 2. Create the repo and push (public)

From this folder, run:

```bash
git init -q && git add -A && git commit -m "Initial commit: AI council template" && gh repo create ai-council-template --public --source=. --remote=origin --push
```

That single line does five things: starts git, stages every file, makes the first commit, creates a **public** GitHub repo named `ai-council-template`, and pushes.

## Options

- **Put it under an organization** (e.g. your `codebridger` org) — name the owner:

  ```bash
  gh repo create codebridger/ai-council-template --public --source=. --remote=origin --push
  ```

- **Make it private instead** — swap `--public` for `--private`.

## 3. (Optional) Move it somewhere nicer

The folder currently sits in a temporary outputs path. After the push, you can clone a fresh copy wherever you keep your projects and delete this one:

```bash
git clone https://github.com/<your-account>/ai-council-template.git
```

## Then set it up

Open the repo and ask your agent to "set up the council". It runs the initializer in `SETUP.md` (Workflow 0) — interviews you (or reads a pitch / PRD you paste) and fills in the whole template for your product, then commits. (Prefer to do it by hand? See `README.md` → "Make it yours".)
