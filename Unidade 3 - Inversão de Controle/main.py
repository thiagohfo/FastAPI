from fastapi import FastAPI, Depends

from api import recipes, users, posts, login, admin, keywords, admin_mcontainer, complaints
from dependencies.global_transactions import log_transaction

app = FastAPI(dependencies=[Depends(log_transaction)])

app.include_router(recipes.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(login.router)
app.include_router(admin.router)
app.include_router(keywords.router)
app.include_router(admin_mcontainer.router)
app.include_router(complaints.router)

@app.get("/")
def index():
    return {"message": "Cooking Recipe Rating Prototype!"}