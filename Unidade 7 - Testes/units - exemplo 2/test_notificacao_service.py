import pytest
from notificacao_service import app
from fastapi.testclient import TestClient
from unittest.mock import patch
import requests_mock

client = TestClient(app)

@pytest.fixture
def mock_email_service():
    with requests_mock.Mocker() as m:
        m.post("http://email-service/enviar/123", status_code=200)
        yield

@patch("notificacao_service.logger")
def test_enviar_notificacao(mock_logger, mock_email_service):
    response = client.post("/notificar/123", json={"mensagem": "Olá"})
    assert response.status_code == 200
    assert response.json() == {"status": "Enviado"}
    mock_logger.info.assert_called_once_with("Notificação enviada para usuário 123")
