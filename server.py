from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import processar

API_PREFIX = '/api'

app = FastAPI(
    title="API Para processar modelo de reconhecimento facial",
    description="Reconhecimento facial",
    version="0.1.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

app.include_router(processar.router, prefix=API_PREFIX)
