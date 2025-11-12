from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.models.ofertas import Oferta
from app.schemas.ofertas import OfertaBase

router = APIRouter(prefix="/ofertas", tags=["Siembra"])


@router.get("/", response_model=list[OfertaBase])
def listar_ofertas(
    response: Response,
    limit: int = Query(50, ge=1, le=200, description="Cantidad de registros a retornar"),
    offset: int = Query(0, ge=0, description="Número de registros a saltar"),
    departamento: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    region: str | None = None,
    ciudad: str | None = None,
    db: Session = Depends(get_db)
):
    base_query = db.query(Oferta)

    if departamento:
        base_query = base_query.filter(normalize(Oferta.Dep_Desc).ilike(f"%{departamento}%"))
    if especie:
        base_query = base_query.filter(normalize(Oferta.Esp_Desc).ilike(f"%{especie}%"))
    if cadena:
        base_query = base_query.filter(normalize(Oferta.Cad_Desc).ilike(f"%{cadena}%"))
    if region:
        base_query = base_query.filter(normalize(Oferta.Reg_Desc).ilike(f"%{region}%"))
    if ciudad:
        base_query = base_query.filter(normalize(Oferta.Ciu_Desc).ilike(f"%{ciudad}%"))

    total = base_query.count()

    data = (
        base_query
        .order_by(Oferta.Ofer_Titulo)
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
