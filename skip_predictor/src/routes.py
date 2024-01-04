from fastapi import APIRouter

from src.predictor_service import SkipPredictServiceDependency
from src.schemas import ModelInput, ModelOutput

predict_router = APIRouter()


@predict_router.post("/predict", response_model=ModelOutput)
def predict(
    request: ModelInput, predict_service: SkipPredictServiceDependency
) -> ModelOutput:
    return predict_service.predict(request)
