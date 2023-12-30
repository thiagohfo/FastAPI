import requests
from fastapi import FastAPI

app = FastAPI()

url_servico_a = "http://localhost:8000"

@app.get("/consumir_compras/{compra_id}")
def consumir_compra(compra_id: int):
    response = requests.get("{}/compras/{}".format(url_servico_a, compra_id))
    if response.status_code == 200:
        return response.json()
    else:
        return {"erro": "Compra não encontrada"}
