from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.db.sqlite_connection import init_sqlite_conn, close_sqlite_conn
from contextlib import asynccontextmanager

from api.routes.router import api_router
from api.settings import logger, settings

# ⬅️ DEFINA O LIFESPAN PRIMEIRO
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_sqlite_conn()   # Startup
    yield                      # A API roda aqui
    await close_sqlite_conn()  # Shutdown

# ✅ ENTÃO PASSE lifespan NA CRIAÇÃO DO APP
app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
    lifespan=lifespan,
)

app.include_router(api_router)

@app.get("/healthcheck")
def healthcheck():
    return JSONResponse(
        status_code=HTTPStatus.OK, content={"status": "OK"}
    )