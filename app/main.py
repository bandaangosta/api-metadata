from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

import psycopg2
import psycopg2.extras
import credentials

app = FastAPI()

subapi = FastAPI(
    root_path="/api/v1",
    title="ASDM execution data API",
    description="Simple REST API for accessing the execution information of a specific ASDM in ALMA Data Warehouse. " + \
                "<p>Intended mainly for analytics and troubleshooting applications.</p>" + \
                "<p>Sync'ed with production database every ~1 hour.</p>"
)
app.mount("/api/v1", subapi)

# Connection string for data warehouse
DSN = "user={} password={} host={} port={} dbname={}".format(
    credentials.user, credentials.password, credentials.host,
    credentials.port, credentials.dbname
)

# Common query handler
def query_uid(sql_query: str, uid: str):
    '''Query handler used for all uid-based queries'''
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

# Custom error handler
@subapi.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse (status_code = 500, content = {"message": "Something went wrong. For correct usage of the API, take a look at /api/v1/docs"})

# Root handlers
@app.get("/")
@app.get("/api")
async def read_main():
    return {"message": "You are possibly looking for the API. Try with /api/v1 or /api/v1/docs"}

# Endpoints
@subapi.get("/execution", summary="Get execution data for a given uid")
async def get_execution(uid: str):
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

