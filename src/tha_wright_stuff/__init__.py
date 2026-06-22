"""tha-wright-stuff: the full tha-* Tabular Helper library family in one install."""

from importlib.metadata import version

__version__ = version("tha-wright-stuff")

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
from tha_google_runner import GoogleError, ThaDocs, ThaDrive, ThaGmail, ThaSheets, ThaSlides
from tha_map_runner import MapperError, ThaMap
from tha_req_runner import ReqError, ThaReq
from tha_snowflake_runner import Session, SnowflakeError, ThaSnowflake, list_profiles
from tha_utils_helper import (
    DateError,
    DictUtils,
    ListUtils,
    NumError,
    StrError,
    ThaDict,
    ThaDT,
    ThaList,
    ThaNum,
    ThaStr,
    ThaType,
    TypeUtils,
    UtilsError,
)

__all__ = [
    "AWSBase",
    "AWSClients",
    "AwsError",
    "BatchCountResult",
    "BatchQueryResult",
    "BatchUpdateResult",
    "ConfigError",
    "DateError",
    "DdbCostTracker",
    "DictUtils",
    "EdfiError",
    "GoogleError",
    "ListUtils",
    "MapperError",
    "NumError",
    "ReqError",
    "Session",
    "SnowflakeError",
    "StrError",
    "ThaCSV",
    "ThaDT",
    "ThaDdb",
    "ThaDict",
    "ThaDocs",
    "ThaDrive",
    "ThaEdfiBase",
    "ThaGmail",
    "ThaGsi",
    "ThaList",
    "ThaMap",
    "ThaNum",
    "ThaReq",
    "ThaS3",
    "ThaSSM",
    "ThaSheets",
    "ThaSlides",
    "ThaSnowflake",
    "ThaStr",
    "ThaStudentAssessment",
    "ThaType",
    "TypeUtils",
    "UtilsError",
    "cli_auth_check",
    "current_identity",
    "list_profiles",
    "parse_arn",
    "parse_assumed_role_arn",
]
