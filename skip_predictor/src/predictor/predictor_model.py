import abc
import pickle
import random
from typing import Any

from sklearn.ensemble import RandomForestClassifier


class AbstractSkipPredictor(abc.ABC):
    @abc.abstractmethod
    def predict(self, x: list) -> str:
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
            return pickle.load(f_handle)


class RandomForestSkipPredictor(AbstractSkipPredictor):
    def __init__(self, model: RandomForestClassifier) -> None:
        self._model = model

    def predict(self, x: list) -> str:
        return self._model.predict(x)

    @property
    def name(self) -> str:
        return "random_forest"

    @classmethod
    def from_pickle(cls, pickle_path: str) -> "AbstractSkipPredictor":
        return cls(cls._load_model(pickle_path))


class MockSkipPredictor(AbstractSkipPredictor):
    def predict(self, x: list) -> str:
        return "yes" if random.randint(0, 1) == 0 else "no"

    @property
    def name(self) -> str:
        return "mock"

    @classmethod
    def from_pickle(cls, pickle_path: str) -> "AbstractSkipPredictor":
        return cls()
