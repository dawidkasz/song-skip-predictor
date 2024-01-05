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

logger = logging.getLogger(__name__)

random_forest_model = RandomForestSkipPredictor.from_pickle("random_forest.pkl")
decision_tree_model = DecisionTreeSkipPredictor.from_pickle("decision_tree.pkl")
mock_model = MockSkipPredictor()


def provide_random_model() -> AbstractSkipPredictor:
    model: AbstractSkipPredictor = (
        random_forest_model if random.randint(0, 1) == 0 else decision_tree_model
    )
    logger.info("Providing %s model using a random strategy", model.name)

    return model


ModelDependency = Annotated[AbstractSkipPredictor, Depends(provide_random_model)]
