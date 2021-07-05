# api-metadata
Simple REST API for ASDM metadata in ALMA Data Warehouse. Intended mainly for analytics and troubleshooting applications.

## Authentication

Copy or rename credentials_sample.py as credentials.py and fill with actual connection data.

## Development
    make run

## Build
    docker build -t api-metadata .

    docker run -d --name api-metadata -p 8080:80 api-metadata

## Endpoints

Visit http://my.server.org:8080/api/docs for API automatically generated documentation.

### metadata
    curl http://my.server.org:8080/api/metadata?uid=uid://A002/Xc384d6/X6c0

    {
      "data": [
        {
          "START_TIME": "2017-08-18T22:50:41.110000+00:00",
          "END_TIME": "2017-08-18T23:48:44.810000+00:00",
          "SB_UID": "uid://A001/X886/Xcc",
          "EB_UID": "uid://A002/Xc384d6/X6c0",
          "EXECUTION_STATUS": "SUCCESS",
          "QA0FLAG": "Pass",
          "ARCHIVING_STATUS": "Complete",
          "IS_CALIBRATION": 0,
          "ALMABUILD": "201608-CYCLE4-ON-B-2017-07-18-00-00-00",
          "IS_TEST": "0",
          "SUBJECT": null,
          "SB_NAME": "triggere_b_07_TM1",
          "PROJECT_CODE": "2016.1.00862.T",
          "PROJECT_NAME": "A Precision Test of Gamma-ray Burst Afterglow Models",
          "ALMA_BAND": "ALMA_RB_07",
          "REF_FREQUENCY": 338.5,
          "STE": "OSF-APE1",
          "ARRAY_NAME": "Array007",
          "ARRAY_TYPE": "Automatic",
          "ARRAY_FAMILY": "12 [m]",
          "CORRELATOR_TYPE": "BL",
          "PHOTONIC_REFERENCE_NAME": "PhotonicReference1",
          "MAIN_ACTIVITY": "PI Observations",
          "ANTENNA_COUNT": 44,
          "ANTENNA_LIST": "DA57,DA55,DA54,DA52,DA50,DV10,DV11,DV13,DV14,DV15,DV17,DV18,PM02,DV19,DA49,DA48,DA47,DA46,DA45,DA44,DA43,DA42,PM04,DA41,PM03,DA62,DA61,DA60,DV20,DV22,DV01,DV23,DV02,DV24,DV03,DV25,DV04,DV05,DV06,DV07,DV08,DV09,DA59,DA58",
          "DA_COUNT": 19,
          "DV_COUNT": 22,
          "PM_COUNT": 3,
          "CM_COUNT": 0,
          "month": "2017-08"
        }
      ],
      "errors": false
    }


### scans
    curl http://my.server.org:8080/api/scans?uid=uid://A002/Xec9a30/X5d70

    {
      "data": [
        {
          "eb_uid": "uid://A002/Xec9a30/X5d70",
          "scan": 1,
          "startTime": "2021-06-05T01:46:02.121",
          "endTime": "2021-06-05T01:51:21.222",
          "numSubscan": 10,
          "scanIntent": "['CALIBRATE_POINTING', 'CALIBRATE_WVR']",
          "sourceName": "J1325-4301",
          "month": "2021-06"
        },
        {
          "eb_uid": "uid://A002/Xec9a30/X5d70",
          "scan": 2,
          "startTime": "2021-06-05T01:51:23.456",
          "endTime": "2021-06-05T01:52:51.455",
          "numSubscan": 3,
          "scanIntent": "['CALIBRATE_ATMOSPHERE', 'CALIBRATE_WVR']",
          "sourceName": "Filament_3_OFF_0",
          "month": "2021-06"
        },
        {
          "eb_uid": "uid://A002/Xec9a30/X5d70",
          "scan": 3,
          "startTime": "2021-06-05T01:52:51.621",
          "endTime": "2021-06-05T02:00:56.561",
          "numSubscan": 55,
          "scanIntent": "['OBSERVE_TARGET']",
          "sourceName": "Filament_1_OFF_0",
          "month": "2021-06"
        },
        ...


