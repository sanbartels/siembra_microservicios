from fastapi import APIRouter
from app.api.endpoints import proyectos

api_router = APIRouter()
api_router.include_router(proyectos.router)
