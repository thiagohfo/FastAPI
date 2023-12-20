import pytest
from pagamento_service import app
from fastapi.testclient import TestClient
from unittest.mock import patch
import requests_mock

client = TestClient(app)

@pytest.fixture
def mock_banco_service():
    with requests_mock.Mocker() as m:
        m.get("http://banco-service/validar/123/100.0", json={"valido": True})
        yield

@patch("pagamento_service.logger")
def test_processar_pagamento(mock_logger, mock_banco_service):
    response = client.post("/pagamento/123", json={"valor": 100.0})
    assert response.status_code == 200
    assert response.json() == {"status": "Sucesso"}
    mock_logger.info.assert_called_once_with("Pagamento processado para usuário 123")
