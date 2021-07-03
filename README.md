# api-metadata
Simple REST API for ASDM metadata in ALMA Data Warehouse

### Development
    make run

### Build
    docker build -t api-metadata .

    docker run -d --name api-metadata -p 8080:80 api-metadata

### Test
    curl http://my.server.org:8080/api/metadata?uid=uid://A002/Xed4607/X9042

    {
    "data": [{
        "START_TIME": "2021-06-28T21:48:41.791000+00:00",
        "END_TIME": "2021-06-28T21:55:59.139000+00:00",
        "SB_UID": "uid://X0/X0/X0",
        "EB_UID": "uid://A002/Xed4607/X9042",
        "EXECUTION_STATUS": "SUCCESS",
        "QA0FLAG": null,
        "ARCHIVING_STATUS": "Complete",
        "IS_CALIBRATION": 0,
        "IS_TEST": "0",
        "SUBJECT": "DelayCal.py -b 3 -s 3c279 -P 4 -d 300 -T -a Array88-ACA --jira CSV-3650",
        "SB_NAME": null,
        "PROJECT_CODE": null,
        "ALMA_BAND": null,
        "REF_FREQUENCY": null,
        "STE": "OSF-APE2",
        "ARRAY_NAME": "Array88-ACA",
        "ARRAY_TYPE": "Manual",
        "ARRAY_FAMILY": "7 [m]",
        "CORRELATOR_TYPE": "ACA",
        "PHOTONIC_REFERENCE_NAME": "PhotonicReference2",
        "MAIN_ACTIVITY": "EOC",
        "ANTENNA_COUNT": 6,
        "ANTENNA_LIST": "CM05,CM03,CM02,CM01,CM11,CM09",
        "DA_COUNT": 0,
        "DV_COUNT": 0,
        "PM_COUNT": 0,
        "CM_COUNT": 6,
        "month": "2021-06"
    }]
}}
