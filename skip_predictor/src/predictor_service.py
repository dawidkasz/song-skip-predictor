import logging
from typing import Annotated

from fastapi import Depends

from src.predictor_model_provider import ModelDependency
from src.schemas import ModelInput, ModelOutput

logger = logging.getLogger(__name__)


class SkipPredictService:
    def __init__(self, predictor: ModelDependency) -> None:
        self._predictor = predictor

    def predict(self, request: ModelInput) -> ModelOutput:
        logger.info(
            "Making prediction using model %s, request: %s",
            type(self._predictor).__name__,
            request,
        )

        prediction = self._predictor.predict(request.to_vector())
        logger.info("Prediction: %s", prediction)

        return ModelOutput(prediction=prediction)


SkipPredictServiceDependency = Annotated[
    SkipPredictService, Depends(SkipPredictService)
]
