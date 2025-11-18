from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.models.ofertas import Oferta
from app.schemas.ofertas import OfertaBase

router = APIRouter(prefix="/ofertas", tags=["Siembra"])

@router.get("", response_model=list[OfertaBase])
def listar_ofertas(
    response: Response,
    limit: int = Query(50, ge=1, le=200, description="Cantidad de registros a retornar"),
    offset: int = Query(0, ge=0, description="Número de registros a saltar"),

    departamento: int | None = Query(None, description="ID del departamento (coincidencia exacta)"),
    ciudad: int | None = Query(None, description="ID de la ciudad (coincidencia exacta)"),
    region: int | None = Query(None, description="ID de la región (coincidencia exacta)"),

    especie: str | None = Query(None, description="Filtro parcial por especie"),
    cadena: str | None = Query(None, description="Filtro parcial por cadena"),

    db: Session = Depends(get_db)
):
    base_query = db.query(Oferta)

    # -------------------------
    # Filtros exactos por ID
    # -------------------------
    if departamento is not None:
        base_query = base_query.filter(Oferta.Dep_Id == departamento)

    if ciudad is not None:
        base_query = base_query.filter(Oferta.Ciu_Cod == ciudad)

    if region is not None:
        # si existe Oferta.Reg_Id lo usamos
        if hasattr(Oferta, "Reg_Id"):
            base_query = base_query.filter(Oferta.Reg_Id == region)
        else:
            base_query = base_query.filter(normalize(Oferta.Reg_Desc).ilike(f"%{region}%"))

    # --------------------------------
    # Filtros textuales flexibles
    # --------------------------------
    if especie:
        base_query = base_query.filter(normalize(Oferta.Esp_Desc).ilike(f"%{especie}%"))

    if cadena:
        base_query = base_query.filter(normalize(Oferta.Cad_Desc).ilike(f"%{cadena}%"))

    # -------------------------
    # Conteo y paginación
    # -------------------------
    total = base_query.count()

    data = (
        base_query
        .order_by(Oferta.Ofer_Titulo)
        .offset(offset)
        .limit(limit)
        .all()
    )

    end = offset + len(data) - 1 if data else offset

    # -------------------------
    # Headers de rango
    # -------------------------
    response.headers["Content-Range"] = f"{offset}-{end}/{total}"
    response.headers["X-Total-Count"] = str(total)
    response.headers["Accept-Ranges"] = "items"

    return data
