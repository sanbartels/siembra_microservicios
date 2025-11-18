from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.models.proyectos import Proyecto
from app.schemas.proyectos import ProyectoBase

router = APIRouter(prefix="/proyectos", tags=["Siembra"])

@router.get("", response_model=list[ProyectoBase])
def listar_proyectos(
    response: Response,
    limit: int = Query(50, ge=1, le=200, description="Cantidad de registros a retornar"),
    offset: int = Query(0, ge=0, description="Número de registros a saltar"),

    departamento: int | None = Query(None, description="ID del departamento (coincidencia exacta)"),
    ciudad: int | None = Query(None, description="ID de la ciudad (coincidencia exacta)"),

    especie: str | None = Query(None, description="Filtro parcial por especie"),
    cadena: str | None = Query(None, description="Filtro parcial por cadena"),

    db: Session = Depends(get_db)
):
    base_query = db.query(Proyecto)

    # Filtros exactos por ID
    if departamento is not None:
        base_query = base_query.filter(Proyecto.Dep_Id == departamento)

    if ciudad is not None:
        base_query = base_query.filter(Proyecto.Ciu_Cod == ciudad)

    # Filtros textuales flexibles
    if especie:
        base_query = base_query.filter(normalize(Proyecto.Esp_Desc).ilike(f"%{especie}%"))

    if cadena:
        base_query = base_query.filter(normalize(Proyecto.Cad_Desc).ilike(f"%{cadena}%"))

    # Conteo total
    total = base_query.count()

    # Datos paginados
    data = (
        base_query.order_by(Proyecto.Proy_Titulo)
        .offset(offset).limit(limit).all()
    )

    # Cabeceras de rango
    end = offset + len(data) - 1 if data else offset
    response.headers["Content-Range"] = f"{offset}-{end}/{total}"
    response.headers["X-Total-Count"] = str(total)
    response.headers["Accept-Ranges"] = "items"

    return data
