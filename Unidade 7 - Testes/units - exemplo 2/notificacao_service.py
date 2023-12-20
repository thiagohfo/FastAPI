from fastapi import FastAPI
import requests
import logging

app = FastAPI()
logger = logging.getLogger("notificacao_service")

@app.post("/notificar/{usuario_id}")
def enviar_notificacao(usuario_id: int, mensagem: str):
    if requests.post(f"http://email-service/enviar/{usuario_id}", json={"mensagem": mensagem}).status_code == 200:
        logger.info(f"Notificação enviada para usuário {usuario_id}")
        return {"status": "Enviado"}
    else:
        return {"status": "Erro"}
