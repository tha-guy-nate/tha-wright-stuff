def test_top_level_imports() -> None:
    from tha_wright_stuff import (
        AWSBase,
        ConfigError,
        DdbCostTracker,
        EdfiError,
        GoogleError,
        MapperError,
        ReqError,
        Session,
        SnowflakeError,
        ThaCSV,
        ThaDdb,
        ThaDict,
        ThaDocs,
        ThaDrive,
        ThaDT,
        ThaEdfiBase,
        ThaGmail,
        ThaGsi,
        ThaList,
        ThaMap,
        ThaNum,
        ThaReq,
        ThaS3,
        ThaSheets,
        ThaSlides,
        ThaSnowflake,
        ThaSSM,
        ThaStr,
        ThaStudentAssessment,
        ThaType,
        UtilsError,
        list_profiles,
    )

    assert ThaCSV is not None
    assert ThaMap is not None
    assert ThaReq is not None
    assert ThaDdb is not None
    assert ThaGsi is not None
    assert ThaS3 is not None
    assert ThaSSM is not None
    assert ThaDict is not None
    assert ThaList is not None
    assert ThaType is not None
    assert ThaStr is not None
    assert ThaNum is not None
    assert ThaDT is not None
    assert ThaStudentAssessment is not None
    assert ThaEdfiBase is not None
    assert ThaSheets is not None
    assert ThaDocs is not None
    assert ThaDrive is not None
    assert ThaSlides is not None
    assert ThaGmail is not None
    assert ThaSnowflake is not None
    assert Session is not None
    assert AWSBase is not None
    assert DdbCostTracker is not None
    assert ConfigError is not None
    assert MapperError is not None
    assert ReqError is not None
    assert UtilsError is not None
    assert EdfiError is not None
    assert GoogleError is not None
    assert SnowflakeError is not None
    assert list_profiles is not None
