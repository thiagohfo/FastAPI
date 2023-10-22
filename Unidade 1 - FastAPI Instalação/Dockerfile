# Usa a imagem oficial do Python como base
FROM python:latest

# Registro do app
LABEL authors="Thiago"

# Define o diretório de trabalho
WORKDIR /app

# Atualiza o pip para a versão mais recente
RUN pip install --upgrade pip

# Copia o código da sua aplicação para o diretório de trabalho no contêiner
COPY .. /app

RUN pip install -r /app/requirements.txt

# Expõe a porta 8000, que é a porta padrão do Uvicorn para o FastAPI
EXPOSE 8000

# Comando padrão para iniciar o servidor Uvicorn com o FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]