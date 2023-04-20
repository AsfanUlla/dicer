from starlite.status_codes import HTTP_200_OK
from starlite.testing import TestClient
import json

def test_jobs_api(test_client: TestClient):
    with test_client as client:
        response = client.get("/jobs")
        assert response.status_code == HTTP_200_OK
        assert "title" in response.json()[0]

def test_jobs_api_limit(test_client: TestClient):
    with test_client as client:
        limit = 5
        response = client.get("/jobs?limit=%s"%str(limit))
        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert len(data) == limit

# TODO Create More tests
