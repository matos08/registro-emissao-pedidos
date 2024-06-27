from loguru import logger

from app.config.bootstrap import create_app
from app.config.db import connect_to_database
from app.config.middlewares import init_middlewares
from app.config.router import init_routers

app = create_app()
init_middlewares(app)


@app.on_event("startup")
async def startup_routers():
    await init_routers(app)
    logger.info("Startup Routers")


@app.on_event("startup")
async def startup_database():
    await connect_to_database()
    logger.info("Startup data base")
