import pytest

from starlite.testing import TestClient

from main import app


@pytest.fixture(scope="function")
def test_client() -> TestClient:
    return TestClient(app=app)