import asyncio

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.config.bootstrap import create_app
from app.config.db import connect_to_database
from app.config.middlewares import init_middlewares
from app.config.router import init_routers
from app.config.settings import get_settings, Settings

settings = get_settings()


def override_settings():
    return Settings(TESTING=True, DB_URL=settings.DB_TEST_URL)


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.dependency_overrides[get_settings] = override_settings()
    register_tortoise(
        app,
        db_url=settings.DB_TEST_URL,
        modules={"models": settings.MODELS},
        generate_schemas=True,
    )

    init_middlewares(app)
    asyncio.run(connect_to_database())
    asyncio.run(init_routers(app))
    with TestClient(app) as test_client:
        yield test_client
