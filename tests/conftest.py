import os

import pytest
from starlette.testclient import TestClient

from seed_data import seed_data, create_db
from server import app

DATABASE_TEST_URL = os.getenv('DATABASE_TEST_URL')
# hack-ist way
os.environ['DATABASE_URL'] = DATABASE_TEST_URL


@pytest.fixture(scope='session')
def client():
    create_db(DATABASE_TEST_URL)
    seed_data(DATABASE_TEST_URL)
    yield TestClient(app)


