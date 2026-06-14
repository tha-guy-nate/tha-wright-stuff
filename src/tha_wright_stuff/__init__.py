"""tha-wright-stuff: the full tha-* Tabular Helper library family in one install."""

from tha_aws_runner import (
    AWSBase,
    AWSClients,
    AwsError,
    BatchCountResult,
    BatchQueryResult,
    BatchUpdateResult,
    DdbCostTracker,
    ThaDdb,
    ThaGsi,
    ThaS3,
    ThaSSM,
    cli_auth_check,
    current_identity,
    parse_arn,
    parse_assumed_role_arn,
)
from tha_csv_runner import ConfigError, ThaCSV
from tha_edfi_runner import EdfiError, ThaEdfiBase, ThaStudentAssessment
from tha_google_runner import GoogleError, ThaSheets
from tha_map_runner import MapperError, ThaMap
from tha_req_runner import ReqError, ThaReq
from tha_snowflake_runner import Session, SnowflakeError, ThaSnowflake, list_profiles
from tha_utils_helper import (
    DateError,
    DictUtils,
    ListUtils,
    NumError,
    StrError,
    ThaDT,
    ThaDict,
    ThaList,
    ThaNum,
    ThaStr,
    ThaType,
    TypeUtils,
    UtilsError,
)

__version__ = "0.1.0"
__all__ = [
    # tha-csv-runner
    "ConfigError",
    "ThaCSV",
    # tha-map-runner
    "MapperError",
    "ThaMap",
    # tha-req-runner
    "ReqError",
    "ThaReq",
    # tha-aws-runner
    "AWSBase",
    "AWSClients",
    "AwsError",
    "BatchCountResult",
    "BatchQueryResult",
    "BatchUpdateResult",
    "DdbCostTracker",
    "ThaDdb",
    "ThaGsi",
    "ThaS3",
    "ThaSSM",
    "cli_auth_check",
    "current_identity",
    "parse_arn",
    "parse_assumed_role_arn",
    # tha-utils-helper
    "ThaDict",
    "ThaList",
    "ThaType",
    "ThaStr",
    "ThaNum",
    "ThaDT",
    "UtilsError",
    "StrError",
    "NumError",
    "DateError",
    "DictUtils",
    "ListUtils",
    "TypeUtils",
    # tha-edfi-runner
    "EdfiError",
    "ThaEdfiBase",
    "ThaStudentAssessment",
    # tha-google-runner
    "GoogleError",
    "ThaSheets",
    # tha-snowflake-runner
    "Session",
    "SnowflakeError",
    "ThaSnowflake",
    "list_profiles",
]
