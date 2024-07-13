from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.settings import Settings
from app.utils import make_aqmp_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await make_aqmp_consumer()
    yield


app = FastAPI(lifespan=lifespan)
