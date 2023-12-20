from fastapi import FastAPI

app = FastAPI()

@app.get("/estoque/{produto_id}")
def verificar_estoque(produto_id: int):
    # Lógica para verificar o estoque
    disponibilidade = True  # Simulação
    return {"disponivel": disponibilidade}
