from fastapi import FastAPI
import requests
import logging

app = FastAPI()
logger = logging.getLogger("pagamento_service")

@app.post("/pagamento/{usuario_id}")
def processar_pagamento(usuario_id: int, valor: float):
    if requests.get(f"http://banco-service/validar/{usuario_id}/{valor}").json()["valido"]:
        logger.info(f"Pagamento processado para usuário {usuario_id}")
        return {"status": "Sucesso"}
    else:
        return {"status": "Falha"}
