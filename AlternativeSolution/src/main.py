from fastapi import FastAPI
import uvicorn
import sys
import os

# Adiciona o diretório 'src' ao sys.path se não estiver presente
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_path not in sys.path:
    sys.path.append(src_path)

from src.chess.api.routes import router
from src.chess.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

# Incluir as rotas da aplicação
app.include_router(router)

# Rota inicial de teste
@app.get("/")
def read_root():
    return {"message": "Welcome to the Chess Data Analysis API"}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
