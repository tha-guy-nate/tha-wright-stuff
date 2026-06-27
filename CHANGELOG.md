# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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