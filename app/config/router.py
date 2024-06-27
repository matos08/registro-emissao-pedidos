from fastapi import FastAPI
from fastapi_pagination import add_pagination


async def init_routers(app: FastAPI):
    from app.modules.core import health_check_router

    app.include_router(health_check_router.router)

    add_pagination(app)
