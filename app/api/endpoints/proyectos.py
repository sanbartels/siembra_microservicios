from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from app.models.proyectos import Proyecto
from app.schemas.proyectos import ProyectoBase

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])

@router.get("/", response_model=list[ProyectoBase])
def listar_proyectos(
    departamento: str | None = Query(None, description="Ej: Cauca (COL) ó cauca"),
    especie: str | None = Query(None, description="Ej: Mojarra, Tilapia, Cobia"),
    cadena: str | None = Query(None, description="Cadena productiva (Cad_Desc)"),
    limit: int | None = Query(None, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Proyecto)

    # 🔥 Filtros flexibles (ilike = case-insensitive + LIKE %valor%)
    if departamento:
        query = query.filter(func.lower(Proyecto.Dep_Desc).ilike(f"%{departamento.lower()}%"))

    if especie:
        query = query.filter(func.lower(Proyecto.Esp_Desc).ilike(f"%{especie.lower()}%"))

    if cadena:
        query = query.filter(func.lower(Proyecto.Cad_Desc).ilike(f"%{cadena.lower()}%"))

    # Ordenar
    query = query.order_by(Proyecto.Proy_Titulo)

    # Paginación opcional (solo si viene limit)
    if limit:
        query = query.limit(limit).offset(offset)

    return query.all()
