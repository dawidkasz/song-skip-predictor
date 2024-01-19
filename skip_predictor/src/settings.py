from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseModel):
    host: str
    port: int
    initdb_root_username: str
    initdb_root_password: str
    db_name: str


class ModelSettings(BaseSettings):
    random_forest_file_path: str
    decision_tree_file_path: str


class Settings(BaseSettings):
    host: str
    port: int
    debug_mode: bool
    db: DbSettings
    model: ModelSettings

    model_config = SettingsConfigDict(env_file=(".env",), env_nested_delimiter="__")


settings = Settings()
