# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.32] - 2026-08-06
### Changed
- Bumped dep floors: tha-snowflake-runner>=0.3.2.

## [0.1.31] - 2026-08-05
### Changed
- Bumped dep floors: tha-snowflake-runner>=0.3.1.

## [0.1.30] - 2026-07-26
### Changed
- Bumped dep floors: tha-edfi-runner>=0.1.9, tha-google-runner>=0.2.2.

## [0.1.29] - 2026-07-19
### Changed
- Bumped dep floors: tha-aws-runner>=0.2.9.

## [0.1.28] - 2026-07-16
### Changed
- Bumped dep floors: tha-snowflake-runner>=0.3.0.

## [0.1.27] - 2026-07-16
### Changed
- Bumped dep floors: tha-map-runner>=0.3.0.

## [0.1.26] - 2026-07-09
### Changed
- Bumped dep floors: tha-csv-runner>=0.4.1.

## [0.1.25] - 2026-07-06
### Changed
- Bumped dep floors: tha-csv-runner>=0.4.0.

## [0.1.24] - 2026-07-05
### Changed
- Bumped dep floors: tha-map-runner>=0.2.12.

## [0.1.23] - 2026-07-05
### Changed
- Bumped dep floors: tha-csv-runner>=0.3.5, tha-map-runner>=0.2.11, tha-req-runner[httpx]>=0.2.7, tha-aws-runner>=0.2.8, tha-edfi-runner>=0.1.8, tha-google-runner>=0.2.1, tha-snowflake-runner>=0.2.3.

## [0.1.22] - 2026-07-04
### Changed
- Bumped dep floors: tha-csv-runner>=0.3.4, tha-map-runner>=0.2.10, tha-req-runner[httpx]>=0.2.6, tha-aws-runner>=0.2.7, tha-edfi-runner>=0.1.7, tha-snowflake-runner>=0.2.2.
### Fixed
- Documented a fix in `tha-github-workflows`' shared `python-ci.yml`: the `Dependency check` step ran `deptry` unconditionally, which broke CI here since this repo deliberately has no `deptry` dev dependency. The step is now guarded on `[tool.deptry]` being present in `pyproject.toml`. No change needed in this repo itself — this entry exists to trigger a CI run confirming the fix.

## [0.1.21] - 2026-07-03
### Added
- `check-yanked-floors.yml` workflow: daily scan of this repo's `tha-*` dependency floors against PyPI's per-release `yanked` status, via the new shared `tha-github-workflows` reusable workflow of the same name; auto-opens/updates/closes a tracking issue here when a floor points at a yanked release.
### Fixed
- `bump-dep-floors.yml` / `dep-floors-check.yml`: the dependency-floor regex didn't account for extras syntax (`pkg[extra]>=X.Y.Z`), so `tha-req-runner[httpx]>=0.2.3` was silently never checked or bumped by either workflow.
- Bumped the now-checked `tha-req-runner[httpx]` floor from `>=0.2.3` to `>=0.2.5` — both 0.2.2 and 0.2.3 are yanked on PyPI; 0.2.5 is the current latest.

## [0.1.20] - 2026-07-03
### Changed
- Bumped dep floors: tha-aws-runner>=0.2.6, tha-snowflake-runner>=0.2.1.

## [0.1.19] - 2026-07-03
### Added
- Python 3.14 classifier and CI support.
- PR template (What/Why/How + Test Plan sections), part of a cross-repo consistency sweep.

## [0.1.18] - 2026-07-03
### Changed
- Bumped dep floors: tha-snowflake-runner>=0.2.0.

## [0.1.17] - 2026-07-03
### Changed
- Bumped dep floors: tha-aws-runner>=0.2.5.

## [0.1.16] - 2026-06-29
### Changed
- `tha-req-runner[httpx]` is now a standard dependency — the `[all]` extra is removed; httpx ships with the base install.

## [0.1.15] - 2026-06-29
### Changed
- Bumped dep floors: tha-csv-runner>=0.3.3.

## [0.1.14] - 2026-06-27
### Changed
- Bumped dep floors to latest PyPI releases: tha-aws-runner>=0.2.3, tha-csv-runner>=0.3.0, tha-map-runner>=0.2.9, tha-utils-helper>=0.2.5, tha-edfi-runner>=0.1.5, tha-google-runner>=0.1.7, tha-snowflake-runner>=0.1.4.

## [0.1.13] - 2026-06-27
### Added
- MIT license file with attribution requirement.
- Auto-tag reusable workflow in CI.
### Changed
- Enabled mypy strict mode for comprehensive type checking.

## [0.1.11] - 2026-06-25
### Added
- Weekly automated dep-floor bump workflow (opens a PR every Friday when any floor lags PyPI).
### Changed
- Updated all tha-* dependency floors to current releases.
- Added pre-commit hooks; centralized publish workflow.

## [0.1.9] - 2026-06-23
### Changed
- Updated tha-snowflake-runner dep floor to >=0.1.3.

## [0.1.8] - 2026-06-22
### Fixed
- Derive __version__ from package metadata instead of hardcoding.

## [0.1.7] - 2026-06-22
### Added
- Dep floors status badge and daily automated check workflow.
- [all] extra that pulls in tha-req-runner[httpx] for the httpx backend.

## [0.1.6] - 2026-06-22
### Changed
- Bumped all tha-* dependency floors to current releases.
- Pinned action versions; trimmed Python 3.14 classifier.

## [0.1.5] - 2026-06-17
### Changed
- Updated tha-google-runner dep floor to >=0.1.5.

## [0.1.4] - 2026-06-16
### Changed
- Updated tha-google-runner dep floor to >=0.1.4.

## [0.1.3] - 2026-06-16
### Added
- ThaDrive, ThaGmail, ThaSlides re-exported from tha-google-runner.
### Changed
- Updated tha-google-runner dep floor to >=0.1.3.

## [0.1.2] - 2026-06-16
### Changed
- Updated tha-google-runner dep floor to >=0.1.2.

## [0.1.1] - 2026-06-16
### Added
- ThaDocs re-exported from tha-google-runner.
### Changed
- Updated tha-google-runner dep floor to >=0.1.1.

## [0.1.0] - 2026-06-14
### Added
- Initial release bundling the full tha-* library family in a single install.
