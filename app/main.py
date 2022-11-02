from fastapi import FastAPI
from users.api import router
from database.db_connect import conn, metadata, engine


app = FastAPI()


app.state.database = conn
metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()

app.include_router(router, prefix='/v1')
