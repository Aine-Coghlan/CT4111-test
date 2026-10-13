---
name: one-fix
description: Fix exactly one buggy exercise file in src/ as a single unit of work - pick a random file, propose the fix, get the user's approval, then open a PR for it. Use when the user asks to fix one exercise, runs /one-fix, or wants a single-file bug-fix PR.
---

# one-fix

Each file in `src/` is a tiny Python exercise containing one deliberate bug. The unit of work for this skill is **one file, one fix, one PR**. Never fix more than one file per run, and never touch any file other than the chosen one.

## Steps

1. **Greet.** Start your reply with exactly:

   > Hello from one-fix skill!

2. **Pick a random file that still has an error.** Skip files that already have a fix in progress (an existing local or remote `fix/<name>` branch):

   ```bash
   git fetch --quiet origin 2>/dev/null
   git branch -a --list '*fix/*'
   python3 -c "import glob, random; print(random.choice(sorted(glob.glob('src/*.py'))))"
   ```

   If the chosen file already has a fix branch or PR, or on reading it you find it has no bug, pick again. If every file is taken, tell the user and stop.

3. **Find the bug.** Read the file, work out what the function is meant to do from its name, and identify the single bug. Keep the fix minimal: change only what is needed to make it correct, keep the existing style, and add no docstrings, comments or tests.

4. **Ask for approval.** Show the user the file name, a one-sentence explanation of the bug, and the proposed change as a diff. Then ask with AskUserQuestion whether to apply it (options: approve, or skip and pick another file). Do not edit anything before they approve. If they choose to skip, go back to step 2. If they pick "Other" with feedback, revise the fix and ask again.

5. **Apply and push.** Once approved:

   ```bash
   git switch main && git pull --ff-only
   git switch -c fix/<name>
   # apply the edit to src/<name>.py
   git add src/<name>.py
   git commit -m "Fix <name>: <short description of bug>"
   git push -u origin fix/<name>
   ```

   Check that `git diff --stat main` shows only `src/<name>.py` before committing. If the push fails, stop after the commit and give the user the `git push` command to run themselves.

6. **Report.** Reply with a one-line summary of the fix and the link for the user to open the PR in their browser: `https://github.com/<owner>/<repo>/pull/new/fix/<name>` (take owner and repo from `git remote get-url origin`). Then switch back to `main`.
