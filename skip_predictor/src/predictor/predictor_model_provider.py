import logging
import random
from typing import Annotated

from fastapi import Depends

from src.predictor.predictor_model import (
    AbstractSkipPredictor,
    DecisionTreeSkipPredictor,
    MockSkipPredictor,
    RandomForestSkipPredictor,
)
from src.settings import settings

logger = logging.getLogger(__name__)

random_forest_model = RandomForestSkipPredictor.from_pickle(
    settings.model.random_forest_file_path
)
decision_tree_model = DecisionTreeSkipPredictor.from_pickle(
    settings.model.decision_tree_file_path
)
mock_model = MockSkipPredictor()


def provide_random_model() -> AbstractSkipPredictor:
    model = random.choice([random_forest_model, decision_tree_model])
    logger.info("Providing %s model using a random strategy", model.name)

    return model


ModelDependency = Annotated[AbstractSkipPredictor, Depends(provide_random_model)]
