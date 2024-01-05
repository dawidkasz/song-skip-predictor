import logging
from typing import Annotated

import pandas as pd
from fastapi import Depends
from sklearn.preprocessing import LabelEncoder

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
        data = self._preprocess_request(request)

        prediction = self._predictor.predict(data)
        logger.info("Prediction: %s", prediction)

        model_output = ModelOutput(prediction=prediction)
        self._predictor_repository.save(self._predictor.name, request, model_output)

        return model_output

    @staticmethod
    def _preprocess_request(request: ModelInput) -> list:
        columns = list(request.model_fields.keys())
        df = pd.DataFrame([request.to_vector()], columns=columns)

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        df["block_duration"] = pd.to_timedelta(df["block_duration"])
        df["session_duration"] = pd.to_timedelta(df["session_duration"])
        df["user_listen_time"] = pd.to_timedelta(df["user_listen_time"])

        label_encoder = LabelEncoder()

        df = df.dropna()
        df["city"] = label_encoder.fit_transform(df["city"])
        df["day"] = df["timestamp"].dt.dayofyear

        df["hourminute"] = df["timestamp"].dt.hour * 60 + df["timestamp"].dt.minute
        df["date_completeness"] = label_encoder.fit_transform(df["date_completeness"])

        df = df.drop(columns=["block_duration", "song_listened"])

        df["session_duration"] = df["session_duration"].apply(
            lambda x: x.total_seconds()
        )
        df["user_listen_time"] = df["user_listen_time"].apply(
            lambda x: x.total_seconds()
        )

        df["premium_user"] = df["premium_user"].astype(int)
        df["isliked"] = df["isliked"].astype(int)
        df["previous_action"] = df["previous_action"].astype(bool).astype(int)

        df = df.drop(columns=["timestamp"])

        print(df.values.tolist())
        return df.values.tolist()


SkipPredictServiceDependency = Annotated[
    SkipPredictService, Depends(SkipPredictService)
]
