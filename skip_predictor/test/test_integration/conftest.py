import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.mongo import mongo_client as mongo_client
from src.settings import settings

TEST_DB_NAME = "db-tests"

DEPENDENCY_OVERRIDES = {}


def _session_setup():
    app.dependency_overrides = DEPENDENCY_OVERRIDES
    settings.db.db_name = TEST_DB_NAME


def _session_teardown():
    pass


@pytest.fixture(autouse=True, scope="session")
def setup_teardown_session_integration():
    _session_setup()
    yield
    _session_teardown()


def _test_setup():
    pass


def _test_teardown():
    mongo_client.drop_database(TEST_DB_NAME)


@pytest.fixture(autouse=True)
def setup_teardown_per_test():
    _test_setup()
    yield
    _test_teardown()


@pytest.fixture
def api_client():
    return TestClient(app)


@pytest.fixture
def mongo_predictions():
    db = mongo_client[settings.db.db_name]
    return db["predictions"]
