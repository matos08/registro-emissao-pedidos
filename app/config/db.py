from loguru import logger
from tortoise import Tortoise

from app.config.settings import get_settings

settings = get_settings()

TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": settings.MODELS,
            "default_connection": "default",
        },
    },
}


async def connect_to_database():
    await Tortoise.init(db_url=settings.DB_URL, modules={"models": settings.MODELS})
    logger.info("Initializer data base")


async def close_connection_database():
    await Tortoise.close_connections()
    logger.info("Close connections data base")
