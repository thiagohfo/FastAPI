import pytest
import requests_mock
from produto_service import app as produto_app
from fastapi.testclient import TestClient

produto_client = TestClient(produto_app)

@pytest.fixture
def mock_estoque_service():
    with requests_mock.Mocker() as m:
        m.get("http://estoque-service/estoque/1", json={"disponivel": True})
        yield

def test_contrato_verificar_produto(mock_estoque_service):
    response = produto_client.get("/produto/1")
    assert response.status_code == 200
    assert response.json() == {"produto_id": 1, "disponibilidade": True}
