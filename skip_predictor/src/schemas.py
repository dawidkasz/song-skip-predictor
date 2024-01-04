from pydantic import BaseModel


class ModelInput(BaseModel):
    pass

    def to_vector(self) -> list:
        return []


class ModelOutput(BaseModel):
    prediction: str
