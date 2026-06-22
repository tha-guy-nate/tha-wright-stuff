# tha-wright-stuff

[![PyPI](https://img.shields.io/pypi/v/tha-wright-stuff)](https://pypi.org/project/tha-wright-stuff/)
[![dep floors](https://github.com/tha-guy-nate/tha-wright-stuff/actions/workflows/dep-floors-check.yml/badge.svg)](https://github.com/tha-guy-nate/tha-wright-stuff/actions/workflows/dep-floors-check.yml)

> Install the entire Tabular Helper (`tha-*`) library family in one shot.

```bash
pip install tha-wright-stuff[all]   # recommended: core family + all optional extras
pip install tha-wright-stuff        # core family only
```

---

## What is this?

`tha-wright-stuff` serves two purposes at once:

### 1. Meta-package

One install pulls in every `tha-*` library and re-exports all of their public symbols from a single namespace. Instead of installing and importing from eight separate packages, you can just do:

```python
# AWS
from tha_wright_stuff import ThaDdb, ThaGsi, ThaS3, ThaSSM, DdbCostTracker, cli_auth_check, current_identity, parse_arn, parse_assumed_role_arn
# CSV
from tha_wright_stuff import ThaCSV
# Ed-Fi
from tha_wright_stuff import ThaEdfiBase, ThaStudentAssessment
# Google
from tha_wright_stuff import ThaSheets, ThaDocs, ThaDrive, ThaSlides, ThaGmail
# Map
from tha_wright_stuff import ThaMap
# Requests
from tha_wright_stuff import ThaReq
# Snowflake
from tha_wright_stuff import ThaSnowflake, Session, list_profiles
# Utils
from tha_wright_stuff import ThaStr, ThaNum, ThaDT, ThaDict, ThaList, ThaType
```

Every public class, function, and error type from all eight libraries is available at the top level.

### 2. Cross-family integration canary

`uv.lock` is intentionally **not committed** to this repo. That means every CI run resolves all eight libraries fresh from PyPI — no pinned snapshot. If any two libraries in the family ship incompatible dependency requirements, this repo's CI will fail, surfacing the conflict before users hit it.

---

## Included libraries

| Package | PyPI | GitHub | What it does |
|---|---|---|---|
| **tha-csv-runner** | [![PyPI](https://img.shields.io/pypi/v/tha-csv-runner)](https://pypi.org/project/tha-csv-runner/) | [tha-csv-runner](https://github.com/tha-guy-nate/tha-csv-runner) | Read and write CSVs with progress bars, header validation, chunking, sort/filter, and an optional per-row validator callback. |
| **tha-map-runner** | [![PyPI](https://img.shields.io/pypi/v/tha-map-runner)](https://pypi.org/project/tha-map-runner/) | [tha-map-runner](https://github.com/tha-guy-nate/tha-map-runner) | Enrich and join dicts using dotted-path projection and O(n+m) index-based lookups. Supports left / inner / anti joins and DynamoDB result shapes. |
| **tha-req-runner** | [![PyPI](https://img.shields.io/pypi/v/tha-req-runner)](https://pypi.org/project/tha-req-runner/) | [tha-req-runner](https://github.com/tha-guy-nate/tha-req-runner) | Transport layer for API runners — session management, retries, `safe_call`, and a normalized `parse_response` dict. Supports both `requests` and `httpx` backends. |
| **tha-aws-runner** | [![PyPI](https://img.shields.io/pypi/v/tha-aws-runner)](https://pypi.org/project/tha-aws-runner/) | [tha-aws-runner](https://github.com/tha-guy-nate/tha-aws-runner) | DynamoDB (`ThaDdb`), GSI queries (`ThaGsi`), S3 (`ThaS3`), SSM Parameter Store (`ThaSSM`), a `DdbCostTracker` context manager that tallies RCU/WCU and USD cost per run, and standalone helpers (`cli_auth_check`, `current_identity`, `parse_arn`, `parse_assumed_role_arn`). |
| **tha-utils-helper** | [![PyPI](https://img.shields.io/pypi/v/tha-utils-helper)](https://pypi.org/project/tha-utils-helper/) | [tha-utils-helper](https://github.com/tha-guy-nate/tha-utils-helper) | Zero-dependency utilities: `ThaStr` (slugify, format), `ThaNum` (currency, parens-as-negative, cast), `ThaDT` (auto-detect date formats), `ThaDict` (pick, omit, rename), `ThaList` (chunk, flatten), `ThaType` (bool/int/float coercion). All include matching `*_rows` batch methods. |
| **tha-edfi-runner** | [![PyPI](https://img.shields.io/pypi/v/tha-edfi-runner)](https://pypi.org/project/tha-edfi-runner/) | [tha-edfi-runner](https://github.com/tha-guy-nate/tha-edfi-runner) | Ed-Fi ODS API client — OAuth client-credentials auth, pagination, and chunked parallel posting via `ThreadPoolExecutor`. |
| **tha-google-runner** | [![PyPI](https://img.shields.io/pypi/v/tha-google-runner)](https://pypi.org/project/tha-google-runner/) | [tha-google-runner](https://github.com/tha-guy-nate/tha-google-runner) | Typed wrappers for Google Sheets (`ThaSheets`), Docs (`ThaDocs`), Drive (`ThaDrive`), Slides (`ThaSlides`), and Gmail (`ThaGmail`) — OAuth2 or ADC auth, read/write/upsert rows, file download, presentation creation, and email sending. |
| **tha-snowflake-runner** | [![PyPI](https://img.shields.io/pypi/v/tha-snowflake-runner)](https://pypi.org/project/tha-snowflake-runner/) | [tha-snowflake-runner](https://github.com/tha-guy-nate/tha-snowflake-runner) | Snowflake query runner (`ThaSnowflake`) — named connection profiles, query execution to row dicts, and chunked parallel inserts. |

---

## Requirements

- Python 3.10+

All eight libraries are installed automatically as dependencies. The `[all]` extra additionally installs optional extras across the family (currently `tha-req-runner[httpx]` for the httpx transport backend).

---

## License

MIT
