from fastapi import FastAPI
import psycopg2
import psycopg2.extras
import credentials

app = FastAPI()
subapi = FastAPI(root_path="/api")

DSN = "user={} password={} host={} port={} dbname={}".format(
    credentials.user, credentials.password, credentials.host,
    credentials.port, credentials.dbname
)

@app.get("/")
def read_main():
    return {"message": "You are possibly looking for the API. Try with /api or /api/docs"}

@subapi.get("/metadata")
async def root(uid: str):
    SQL = """
       SELECT *
         FROM "public"."eb_uid_execution_info"
        WHERE "EB_UID" = %s;
    """

    with psycopg2.connect(DSN) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
            curs.execute(SQL, [uid])
            _results = curs.fetchall()
            results = [{k:v for k, v in record.items()} for record in _results]
    return {"data": results}

@subapi.get("/scans")
async def root(uid: str):
    SQL = """
       SELECT *
         FROM "public"."asdm_scan_table"
        WHERE "eb_uid" = %s;
    """

    with psycopg2.connect(DSN) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
            curs.execute(SQL, [uid])
            _results = curs.fetchall()
            results = [{k:v for k, v in record.items()} for record in _results]
    return {"data": results}


app.mount("/api", subapi)
