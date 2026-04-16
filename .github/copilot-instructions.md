<!-- Repository wide instructions for Copilot -->

# Repository-Wide Copilot Instructions

## Verify Copilot is using instructions files

After each user interaction, say which files you have read and used below .github folder.

## Update README.md

After each user interaction, update `README.md` to reflect the changes mad, if needed.

## Path-Specific Instructions

This repository uses path-specific custom instructions to enforce different workflows depending on which folder you are modifying.

### When modifying `app/` folder

**Always consult and follow** [.github/instructions/app.instructions.md](.github/instructions/app.instructions.md) before making any changes to files under `app/`.

Current requirements:
- TDD (Test-Driven Development) workflow is mandatory
- Write failing tests first, then production code
- Aim for 100% line and branch coverage

### When modifying `tests/` folder

**Always consult and follow** [.github/instructions/tests.instructions.md](.github/instructions/tests.instructions.md) before making any changes to files under `tests/`.

Current requirements:
- Every new test function must include an author header (`# Author:` and `# Date:`) immediately above the function signature
- Author name comes from `git config user.name`
- Date format is `YYYY-MM-DD`

### How to use path-specific instructions

1. Before making changes to any file, identify its folder
2. Check if there's a corresponding instructions file in `.github/instructions/`
3. Read and follow that file's rules before implementing changes
4. These instructions take precedence over general guidance

## AI Decision Records (ADRs)

After completing any non-trivial task (implementing a feature, creating a file, changing instructions, refactoring, fixing a bug), create an **AI Decision Record** in `log/`.

### Why ADRs instead of raw context dumps

Raw context is noisy and hard to reuse. A structured ADR captures intent, rationale, and outcome in a form any AI assistant can load as grounding context on a future session. It also serves as a human-readable audit trail.

### File naming

```
log/YYYY-MM-DD-<short-slug>.md
```

- `YYYY-MM-DD` — today's date
- `<short-slug>` — 3–5 word kebab-case summary of the task (e.g., `add-tdd-skill`, `update-test-instructions`)
- If multiple records are created on the same day, append `-2`, `-3`, etc.

### ADR template

Every record must follow this exact structure:

```markdown
# <Title: one sentence describing what was done>

**Date:** YYYY-MM-DD  
**Author:** <output of `git config user.name`>  
**Status:** Done

## Request

> Paste or paraphrase the user's original request here.

## Decision

What was implemented or changed, and why this approach was chosen over alternatives.

## Files Changed

| File | Change |
|------|--------|
| `path/to/file.py` | Brief description of what changed |

## What Was NOT Done

Any reasonable alternative that was deliberately excluded, and why.

## Reuse Notes

Key facts a future AI assistant would need to continue this work or understand the context:
- ...
```

### When to create a record

Create a record when the task involves **any** of:
- Creating or modifying source files under `app/` or `tests/`
- Creating or modifying instruction files under `.github/`
- Creating skills under `.github/skills/`
- Any multi-step workflow that produces lasting changes

Skip for: read-only queries, quick one-liner fixes, and purely conversational answers.

### Storage and version control

The `log/` folder is listed in `.gitignore` — records are **local only** and never committed. They exist solely as reusable context for AI sessions on the current machine.

### Keeping records useful

- Be concise. Each section should be 1–5 lines unless complexity demands more.
- Write for an AI reader: use precise file paths, function names, and exact terminology.
- Do not summarise the entire conversation — only capture the decision and its rationale.