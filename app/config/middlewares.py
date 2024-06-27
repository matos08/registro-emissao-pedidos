from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import get_settings

setting = get_settings()


def init_middlewares(app: FastAPI):
    """

    :param app: Object fastapi.FastAPI
    :return: None
    """
    app.add_middleware(CORSMiddleware,
                       allow_credentials=True,
                       allow_origins=setting.ORIGINS,
                       allow_methods=setting.ALLOW_METHODS,
                       allow_headers=setting.ALLOW_HEADERS)
