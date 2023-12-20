from fastapi import FastAPI
import requests
import logging

app = FastAPI()
logger = logging.getLogger("reserva_service")

@app.post("/reservar/{item_id}")
def reservar_item(item_id: int):
    if requests.get(f"http://estoque-service/verificar/{item_id}").json()["disponivel"]:
        logger.info(f"Item {item_id} reservado com sucesso")
        return {"status": "Reservado"}
    else:
        return {"status": "Indisponível"}
