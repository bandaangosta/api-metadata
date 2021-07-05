from fastapi import FastAPI
import psycopg2
import psycopg2.extras
import credentials

app = FastAPI()

subapi = FastAPI(
    root_path="/api",
    title="ASDM metadata API",
    description="Simple REST API for ASDM metadata in ALMA Data Warehouse. " + \
                "Intended mainly for analytics and troubleshooting applications. " + \
                "Sync'ed with production database every ~1 hour."
)

DSN = "user={} password={} host={} port={} dbname={}".format(
    credentials.user, credentials.password, credentials.host,
    credentials.port, credentials.dbname
)

def query_uid(sql_query: str, uid: str):
    try:
        with psycopg2.connect(DSN) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
                curs.execute(sql_query, [uid])
                _results = curs.fetchall()
                results = [{k:v for k, v in record.items()} for record in _results]
        conn.close()
    except Exception:
        errors = True
    else:
        errors = False

    return {"results": results, "errors": errors}


@app.get("/")
async def read_main():
    return {"message": "You are possibly looking for the API. Try with /api or /api/docs"}

@subapi.get("/metadata", summary="Get metadata for a given uid")
async def get_metadata(uid: str):
    SQL = """
       SELECT *
         FROM "public"."eb_uid_execution_info"
        WHERE "EB_UID" = %s;
    """

    data = query_uid(SQL, uid)

    return {
        "data": data["results"],
        "errors": data["errors"]
    }

@subapi.get("/scans", summary="Get list of scans for a given uid")
async def get_scans(uid: str):
    SQL = """
       SELECT *
         FROM "public"."asdm_scan_table"
        WHERE "eb_uid" = %s;
    """

    data = query_uid(SQL, uid)

    return {
        "data": data["results"],
        "errors": data["errors"]
    }

app.mount("/api", subapi)
