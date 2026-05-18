# Development Guide Plan

This section is for maintainers/contributors, not end users.

## Recommended Location

- Keep developer-only documentation under `docs/development/`.
- Keep user-facing usage and installation in the root `README.md`.

## Documentation Plan

- [ ] **Development environment setup**
  - Python version policy and `uv` usage.
  - Creating/syncing the virtual environment.
  - Installing dev dependencies.

- [ ] **Run tests**
  - Command(s) to run all tests.
  - Command(s) to run a single file/test.
  - Any required environment variables/mocks.

- [ ] **Quality checks**
  - Lint/format/type-check commands (if adopted).
  - Expected output and failure handling.

- [ ] **Build/freeze Linux binary**
  - Prerequisites for Linux build host.
  - Exact freeze/build commands.
  - Output paths and artifact naming.

- [ ] **Build/freeze Windows binary**
  - Preferred approach (native Windows or cross-build policy).
  - Exact freeze/build commands.
  - Output paths and artifact naming.

- [ ] **Release process**
  - Version bump steps and source-of-truth rule.
  - Changelog update steps.
  - Where binaries are published (`releases/` vs GitHub Releases).

- [ ] **Troubleshooting**
  - Garmin auth/token cache issues.
  - `cx_Freeze` packaging issues.
  - Platform-specific dependency issues.

## Proposed Next Files

- `docs/development/testing.md`
- `docs/development/build-linux.md`
- `docs/development/build-windows.md`
- `docs/development/release.md`

Once these files exist, add a "Developer docs" link in `README.md`.
