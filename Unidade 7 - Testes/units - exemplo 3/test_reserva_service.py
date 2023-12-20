import pytest
from reserva_service import app
from fastapi.testclient import TestClient
from unittest.mock import patch
import requests_mock

client = TestClient(app)

@pytest.fixture
def mock_estoque_service():
    with requests_mock.Mocker() as m:
        m.get("http://estoque-service/verificar/1", json={"disponivel": True})
        yield

@patch("reserva_service.logger")
def test_reservar_item(mock_logger, mock_estoque_service):
    response = client.post("/reservar/1")
    assert response.status_code == 200
    assert response.json() == {"status": "Reservado"}
    mock_logger.info.assert_called_once_with("Item 1 reservado com sucesso")
