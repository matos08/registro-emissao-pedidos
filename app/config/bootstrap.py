from fastapi import FastAPI

from app.config.settings import get_settings

setting = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(title=setting.APP_NAME, version=setting.APP_VERSION,
                  description=setting.APP_DESCRIPTION, root_path=setting.APP_ROOT_PATH)
    return app
