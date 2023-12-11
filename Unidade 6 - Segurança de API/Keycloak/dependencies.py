from fastapi import HTTPException, Cookie

def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Não autorizado")

    return access_token
