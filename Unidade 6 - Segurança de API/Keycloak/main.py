from fastapi import FastAPI, Depends
import keycloak_auth
from services import service_a, service_b
from dependencies import get_current_user

app = FastAPI()

app.include_router(keycloak_auth.router)
app.include_router(service_a.router)
app.include_router(service_b.router)

@app.get("/protected")
async def protected_route(user=Depends(get_current_user)):
    return {"message": "Você está autenticado"}
