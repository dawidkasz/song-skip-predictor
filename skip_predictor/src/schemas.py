from pydantic import BaseModel


class ModelInput(BaseModel):
    isliked: bool
    timestamp: str
    previous_song_listened: float
    song_listened_rate: float
    session_duration: str
    session_skip_count: int
    session_like_count: int
    session_play_count: int
    session_skip_rate: float
    session_ewma_rate: float
    previous_action: bool
    user_listen_time: str
    user_skip_count: int
    user_like_count: int
    user_play_count: int
    user_skip_rate: float
    user_ewma_rate: float
    user_listened_rate: float
    city: str
    premium_user: bool
    popularity: int
    release_year: int
    release_daymonth: int
    date_completeness: str
    duration_ms: int
    MUSIC1: float
    MUSIC2: float
    fav_genres_similarity: int

    def to_vector(self) -> list:
        return [getattr(self, field) for field in self.model_fields]


class ModelOutput(BaseModel):
    isskipped: bool
