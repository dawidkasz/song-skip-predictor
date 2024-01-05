import logging
import random
from typing import Annotated

from fastapi import Depends

from src.predictor.predictor_model import (
    AbstractSkipPredictor,
    MockSkipPredictor,
    RandomForestSkipPredictor,
)

logger = logging.getLogger(__name__)


class MockRandomForestLoadedFromPickle:
    def predict(self, x):
        return "yes"


random_forest_model = RandomForestSkipPredictor(MockRandomForestLoadedFromPickle())
mock_model = MockSkipPredictor()


def provide_random_model() -> AbstractSkipPredictor:
    model: AbstractSkipPredictor = (
        random_forest_model if random.randint(0, 1) == 0 else mock_model
    )
    logger.info("Providing %s model using a random strategy", model.name)

    return model


ModelDependency = Annotated[AbstractSkipPredictor, Depends(provide_random_model)]
