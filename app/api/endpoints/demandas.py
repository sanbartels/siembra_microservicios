from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.models.demandas import Demanda
from app.schemas.demandas import DemandaBase

router = APIRouter(prefix="/demandas", tags=["Siembra"])


@router.get("/", response_model=list[DemandaBase])
def listar_demandas(
    response: Response,
    limit: int = Query(50, ge=1, le=200, description="Cantidad de registros a retornar"),
    offset: int = Query(0, ge=0, description="Número de registros a saltar"),
    departamento: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    region: str | None = None,
    db: Session = Depends(get_db)
):
    base_query = db.query(Demanda)

    if departamento:
        base_query = base_query.filter(normalize(Demanda.Dep_Desc).ilike(f"%{departamento}%"))
    if especie:
        base_query = base_query.filter(normalize(Demanda.Esp_Desc).ilike(f"%{especie}%"))
    if cadena:
        base_query = base_query.filter(normalize(Demanda.Cad_Desc).ilike(f"%{cadena}%"))
    if region:
        base_query = base_query.filter(normalize(Demanda.Reg_Desc).ilike(f"%{region}%"))

    total = base_query.count()

    data = (
        base_query
        .order_by(Demanda.Dem_Titulo)
        .offset(offset)
        .limit(limit)
        .all()
    )

    end = offset + len(data) - 1 if data else offset

    # ✅ Headers estandarizados IM
    response.headers["Content-Range"] = f"items {offset}-{end}/{total}"
    response.headers["X-Total-Count"] = str(total)
    response.headers["Accept-Ranges"] = "items"

    return data
