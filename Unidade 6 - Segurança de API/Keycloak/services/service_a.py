from fastapi import APIRouter, Depends
from dependencies import get_current_user

router = APIRouter()

@router.get("/service-a", dependencies=[Depends(get_current_user)])
async def read_service_a():
    return {"message": "Service A"}
