from typing import Annotated

from fastapi import Depends
from pymongo import MongoClient
from pymongo.client_session import ClientSession

from src.settings import settings

mongo_client: MongoClient = MongoClient(host=settings.db.host, port=settings.db.port)


def create_db_session() -> ClientSession:
    return mongo_client.start_session()


DbSession = Annotated[ClientSession, Depends(create_db_session)]
