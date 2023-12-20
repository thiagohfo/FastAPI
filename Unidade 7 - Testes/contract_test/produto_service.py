from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/produto/{produto_id}")
def verificar_produto(produto_id: int):
    response = requests.get(f"http://estoque-service/estoque/{produto_id}")
    return {"produto_id": produto_id, "disponibilidade": response.json()['disponivel']}
