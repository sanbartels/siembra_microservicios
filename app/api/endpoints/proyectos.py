from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.models.proyectos import Proyecto
from app.schemas.proyectos import ProyectoBase

router = APIRouter(prefix="/proyectos", tags=["Siembra"])

@router.get("/", response_model=list[ProyectoBase])
def listar_proyectos(
    response: Response,
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    departamento: str | None = None,
    ciudad: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    db: Session = Depends(get_db)
):
    base_query = db.query(Proyecto)

    if departamento:
        base_query = base_query.filter(normalize(Proyecto.Dep_Id).ilike(f"%{departamento}%"))

    if especie:
        base_query = base_query.filter(normalize(Proyecto.Esp_Desc).ilike(f"%{especie}%"))

    if cadena:
        base_query = base_query.filter(normalize(Proyecto.Cad_Desc).ilike(f"%{cadena}%"))

    if ciudad:
        base_query = base_query.filter(normalize(Proyecto.Ciu_Cod).ilike(f"%{ciudad}%"))

    total = base_query.count()

    data = (
        base_query.order_by(Proyecto.Proy_Titulo)
        .offset(offset).limit(limit).all()
    )

    end = offset + len(data) - 1 if data else offset

    response.headers["Content-Range"] = f"{offset}-{end}/{total}"
    response.headers["X-Total-Count"] = str(total)
    response.headers["Accept-Ranges"] = "items"

    return data
