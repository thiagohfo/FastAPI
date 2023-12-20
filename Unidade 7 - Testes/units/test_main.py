import pytest
from unittest.mock import patch
import requests_mock
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture
def mock_external_service():
    with requests_mock.Mocker() as m:
        m.get("https://externalservice.com/data", json={"key": "value"})
        yield

@patch("main.logger")
def test_read_data(mock_logger, mock_external_service):
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json() == {"key": "value"}
    mock_logger.info.assert_called_once_with("Acessando dados externos.")
