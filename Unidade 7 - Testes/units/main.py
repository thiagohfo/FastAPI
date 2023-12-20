from fastapi import FastAPI
import requests
import logging

app = FastAPI()
logger = logging.getLogger("meu_logger")

def get_external_data():
    response = requests.get("https://externalservice.com/data")
    return response.json()

@app.get("/data")
def read_data():
    logger.info("Acessando dados externos.")
    return get_external_data()
