import logging
from typing import Annotated

from fastapi import Depends

from src.predictor.precitor_repository import PredictorRepositoryDependency
from src.predictor.predictor_model_provider import ModelDependency
from src.schemas import ModelInput, ModelOutput

logger = logging.getLogger(__name__)


class SkipPredictService:
    def __init__(
        self,
        predictor: ModelDependency,
        predictor_repository: PredictorRepositoryDependency,
    ) -> None:
        self._predictor = predictor
        self._predictor_repository = predictor_repository

    def predict(self, request: ModelInput) -> ModelOutput:
        logger.info(
            "Making prediction using model %s, request: %s",
            self._predictor.name,
            request,
        )

        prediction = self._predictor.predict(request.to_vector())
        logger.info("Prediction: %s", prediction)

        model_output = ModelOutput(prediction=prediction)
        self._predictor_repository.save(self._predictor.name, request, model_output)

        return model_output


SkipPredictServiceDependency = Annotated[
    SkipPredictService, Depends(SkipPredictService)
]
