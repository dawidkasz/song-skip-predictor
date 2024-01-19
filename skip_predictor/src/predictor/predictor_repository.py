import abc
import logging
from typing import Annotated

from fastapi import Depends

from src.mongo import DbSession
from src.schemas import ModelInput, ModelOutput
from src.settings import settings

logger = logging.getLogger(__name__)


class AbstractPredictorRepository(abc.ABC):
    @abc.abstractmethod
    def save(
        self, model_name: str, model_input: ModelInput, model_output: ModelOutput
    ) -> None:
        pass


class PredictorRepositoryMongo(AbstractPredictorRepository):
    COLLECTION_NAME = "predictions"

    def __init__(self, session: DbSession) -> None:
        self._session = session
        self._mongo_client = self._session.client
        self._db = self._mongo_client[settings.db.db_name]
        self.collection = self._db[self.COLLECTION_NAME]

    def save(
        self, model_name: str, model_input: ModelInput, model_output: ModelOutput
    ) -> None:
        logger.debug("Saving prediction result of model %s to mongodb", model_name)
        self.collection.insert_one(
            {
                "model": model_name,
                "input": model_input.model_dump(),
                "output": model_output.model_dump(),
            }
        )


PredictorRepositoryDependency = Annotated[
    AbstractPredictorRepository, Depends(PredictorRepositoryMongo)
]
