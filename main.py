from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import (usuario, auth_router, unidades_medida, metodos_pago)

from utils.app_exceptions import app_exception_handler, AppExceptionCase

app = FastAPI(
    title="API PDV",
    description="API para gestión de punto de venta oh yeah",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(AppExceptionCase, app_exception_handler)

app.include_router(auth_router.router)
app.include_router(usuario.router)
app.include_router(unidades_medida.router)
app.include_router(metodos_pago.router)


@app.get("/")
def root():
    return {
        "message": "API PDV",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
