from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
import httpx
import os

router = APIRouter()

@router.get("/login")
async def login_via_keycloak(request: Request):
    client_id = "microservice_test"
    redirect_uri = "http://localhost:8000/callback"
    return RedirectResponse(url=f"http://localhost:8080/auth/realms/sistemascorporativos/protocol/openid-connect/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

@router.get("/callback")
async def callback(code: str, request: Request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "microservice_test",
        "client_secret": "qqV2BMvB6FvchuhJCiVkt54AVFLolx3G",
        "code": code,
        "redirect_uri": "http://localhost:8000/callback"
    }
    response = httpx.post("http://localhost:8080/auth/realms/sistemascorporativos/protocol/openid-connect/token", data=data)
    response.raise_for_status()
    access_token = response.json()["access_token"]
    response = RedirectResponse(url="/protected")
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response

@router.get("/logout")
async def logout(request: Request):
    response = RedirectResponse(url="/")
    response.delete_cookie(key="access_token")
    return response
