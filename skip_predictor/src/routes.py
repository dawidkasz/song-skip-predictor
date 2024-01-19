from fastapi import APIRouter

from src.predictor.predictor_service import SkipPredictServiceDependency
from src.schemas import ModelInput, ModelOutput

predict_router = APIRouter()


@predict_router.post("/predict", response_model=ModelOutput)
def predict(
    request: ModelInput, predict_service: SkipPredictServiceDependency
) -> ModelOutput:
    """Predicts whether user will skip the song"""

    return predict_service.predict(request)
