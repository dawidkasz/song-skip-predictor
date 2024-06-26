import abc
import random
from typing import Any

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class AbstractSkipPredictor(abc.ABC):
    @abc.abstractmethod
    def predict(self, x: pd.DataFrame) -> bool:
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @classmethod
    @abc.abstractmethod
    def from_pickle(cls, pickle_path: str) -> "AbstractSkipPredictor":
        pass

    @staticmethod
    def _load_model(pickle_path: str) -> Any:
        with open(pickle_path, "rb") as f_handle:
            return joblib.load(f_handle)


class RandomForestSkipPredictor(AbstractSkipPredictor):
    def __init__(self, model: RandomForestClassifier) -> None:
        self._model = model

    def predict(self, x: pd.DataFrame) -> bool:
        return bool(self._model.predict(x)[0])

    @property
    def name(self) -> str:
        return "random_forest"

    @classmethod
    def from_pickle(cls, pickle_path: str) -> "AbstractSkipPredictor":
        return cls(cls._load_model(pickle_path))


class DecisionTreeSkipPredictor(AbstractSkipPredictor):
    def __init__(self, model: RandomForestClassifier) -> None:
        self._model = model

    def predict(self, x: pd.DataFrame) -> bool:
        return bool(self._model.predict(x)[0])

    @property
    def name(self) -> str:
        return "decision_tree"

    @classmethod
    def from_pickle(cls, pickle_path: str) -> "AbstractSkipPredictor":
        return cls(cls._load_model(pickle_path))


class MockSkipPredictor(AbstractSkipPredictor):
    def predict(self, x: pd.DataFrame) -> bool:
        return bool(random.randint(0, 1))

    @property
    def name(self) -> str:
        return "mock"

    @classmethod
    def from_pickle(cls, pickle_path: str) -> "AbstractSkipPredictor":
        return cls()
