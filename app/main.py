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
SQL = """
   SELECT *
     FROM "public"."eb_uid_execution_info"
    WHERE "EB_UID" = %s;
"""
eb_uid = 'uid://A002/Xc384d6/X6c0'

@app.get("/")
def read_main():
    return {"message": "You are possibly looking for the API. Try with /api or /api/docs"}

@subapi.get("/metadata")
async def root(uid: str):
    with psycopg2.connect(DSN) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
            curs.execute(SQL, [uid])
            _results = curs.fetchall()
            results = [{k:v for k, v in record.items()} for record in _results]
            details = curs.description
    return {"data": results}

@subapi.get("/scans")
async def root(uid: str):
    return {"data": "not implemented"}

app.mount("/api", subapi)