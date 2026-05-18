# Garmin Backup Improvement Tasks

Use this checklist to track independent improvements. You can complete any item in any order.

Status legend used in this file:
- `done`: task completed
- `skipped`: intentionally not doing it right now
- `deferred`: planned for later

- [ ] **Task 1: Fix CLI entry point packaging** *(currently skipped; see `docs/assistant/DECISIONS.md`)*
  - Rename the runtime module to a valid Python import name (for example `src/garmin_backup.py`).
  - Update the script entry point in `pyproject.toml` to `garmin-backup = "garmin_backup:main"`.
  - Keep the CLI command name as `garmin-backup` for end users.
  - Verify with a clean install and `garmin-backup --help`.

- [ ] **Task 2: Add safe auth failure handling**
  - Handle cases where API initialization fails.
  - Exit gracefully with a clear error message and non-zero status.
  - Avoid `NoneType` crashes when login/authentication fails.
  - Verify by testing with invalid credentials.

- [ ] **Task 3: Unify version source**
  - Remove version drift between `pyproject.toml`, runtime `__version__`, and build config.
  - Choose one source of truth for versioning.
  - Ensure `--version` output and packaging metadata match.

- [ ] **Task 4: Improve credential environment variables**
  - Replace generic `USER` / `PASSWORD` usage with app-specific names (`GARMIN_USERNAME`, `GARMIN_PASSWORD`).
  - Optionally keep backward compatibility with legacy names.
  - Update CLI help text and documentation accordingly.

- [ ] **Task 5: Harden path and input validation**
  - Strengthen path validation (`click.Path`) for writable directory targets.
  - Add validation that start date is not after end date.
  - Normalize missing activity names across all download paths.

- [ ] **Task 6: Make downloads fault-tolerant**
  - Catch and report per-activity/per-format download failures.
  - Continue with remaining downloads when individual files fail.
  - Print a final summary of successes and failures.
  - Optionally retry transient HTTP failures.

- [ ] **Task 7: Standardize output and verbosity**
  - Consolidate mixed `print` and `logging` output patterns.
  - Map verbosity levels consistently to output detail.
  - Keep progress behavior predictable for interactive and scripted use.

- [ ] **Task 8: Add focused automated tests**
  - Add tests for `DateOrYear`, `sanitize`, and `generate_activity_name`.
  - Add tests for filtering and `MAX_ACTIVITIES` cap logic.
  - Mock Garmin API behavior for id/date-based flows.

- [ ] **Task 9: Refresh README and usage docs**
  - Align examples with the canonical installed CLI usage.
  - Update environment variable names and authentication notes.
  - Fix minor wording and consistency issues in option descriptions.

- [ ] **Task 10: Clean release/build metadata**
  - Update stale build metadata text in `setup.py`.
  - Decide and document whether binary artifacts stay in git or only in GitHub Releases.
  - Document release naming/version conventions.

- [ ] **Task 11: Add developer documentation (non-user workflows)**
  - Create a dedicated developer guide for local development and release workflows.
  - Document test commands and test environment setup.
  - Document freeze/build steps for Linux and Windows binaries.
  - Add troubleshooting notes for common build/auth dependency issues.
  - Link developer docs from the main `README.md`.
