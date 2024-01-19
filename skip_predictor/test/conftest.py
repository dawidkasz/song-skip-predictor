from contextlib import contextmanager

import pytest

from src.app import app


@contextmanager
def dependency_overrider(override: dict):
    previous_overrides = app.dependency_overrides.copy()
    for dependency, new_override in override.items():
        app.dependency_overrides[dependency] = new_override

    yield

    app.dependency_overrides = previous_overrides


@pytest.fixture
def override_dependency():
    return dependency_overrider


@pytest.fixture
def raw_model_payload():
    return {
        "isliked": False,
        "timestamp": "2019-11-21 04:42:00.673600",
        "previous_song_listened": 1.0,
        "song_listened_rate": 1.0,
        "session_duration": "0 days 00:00:00",
        "session_skip_count": 0,
        "session_like_count": 0,
        "session_play_count": 0,
        "session_skip_rate": 0.0,
        "session_ewma_rate": 0.0,
        "previous_action": False,
        "user_listen_time": "0 days 00:00:00",
        "user_skip_count": 0,
        "user_like_count": 0,
        "user_play_count": 0,
        "user_skip_rate": 0.0,
        "user_ewma_rate": 0.0,
        "user_listened_rate": 1.0,
        "city": "Krakow",
        "premium_user": True,
        "popularity": 29,
        "release_year": 1992,
        "release_daymonth": 284,
        "date_completeness": "full_date",
        "duration_ms": 228267,
        "MUSIC1": -1.3573162878,
        "MUSIC2": 1.1269005166,
        "fav_genres_similarity": 2,
    }
