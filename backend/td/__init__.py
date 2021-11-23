import motor.motor_asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from beanie import init_beanie

from .config import settings
from td.apps.documents.document import Round, User, Game, GamePlayer
from td.apps.routers.game import router
from td.apps.server.server import sio, app


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.mount("/sub", app)

    @app.on_event("startup")
    async def startup_event():
        client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
        await init_beanie(database=client[settings.MONGODB_DATABASE_NAME], document_models=[Game, User, Round, GamePlayer])

    return app