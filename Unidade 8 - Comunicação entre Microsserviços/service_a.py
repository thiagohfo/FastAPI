from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Categoria(BaseModel):
    nome: str

class Produto(BaseModel):
    nome: str

class Compra(BaseModel):
    id: Optional[int]
    categorias: List[Categoria]
    produtos: List[Produto]

compras_db = []

class CategoriaCreate(BaseModel):
    nome: str

class ProdutoCreate(BaseModel):
    nome: str

class CompraCreate(BaseModel):
    categorias: List[CategoriaCreate]
    produtos: List[ProdutoCreate]

@app.post("/compras/", response_model=int)
def criar_compra(compra_data: CompraCreate):
    nova_compra = Compra(
        id=len(compras_db) + 1,
        categorias=[Categoria(nome=categoria.nome) for categoria in compra_data.categorias],
        produtos=[Produto(nome=produto.nome) for produto in compra_data.produtos])
    compras_db.append(nova_compra)
    return nova_compra.id

@app.get("/compras/{compra_id}")
def get_compra(compra_id: int):
    compra = next((c for c in compras_db if c.id == compra_id), None)
    if compra is None:
        raise HTTPException(status_code=404, detail="Compra não encontrada")
    return compra
