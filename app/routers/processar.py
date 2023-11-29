from fastapi import APIRouter, File, UploadFile, HTTPException
from pydantic import BaseModel
import os
import shutil
from ..services.processar_modelo import prever_pessoa
router = APIRouter()

class ResultadoPredicao(BaseModel):
    mensagem: str
    pessoa_prevista: str

@router.post("/processar/")
async def processar_imagem(file: UploadFile = File(...)):
    try:

        img_path = f"uploads/{file.filename}"
        os.makedirs("uploads", exist_ok=True)

        with open(img_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        predicted_name = prever_pessoa(img_path)
        print(f"Resultados para a imagem {img_path}: {predicted_name}")

        return ResultadoPredicao(mensagem="Sucesso", pessoa_prevista=predicted_name)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")