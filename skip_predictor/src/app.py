import logging.config

from fastapi import FastAPI

from src.routes import predict_router
from src.settings import settings

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)


app = FastAPI(debug=settings.debug_mode)

app.include_router(predict_router, prefix="")
