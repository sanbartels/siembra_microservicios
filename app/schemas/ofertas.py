from pydantic import BaseModel

class OfertaBase(BaseModel):
    OferTbl_Id: int
    Ofer_Id: int | None = None
    Ofer_Titulo: str | None = None
    Ofer_Desc: str | None = None

    Esp_Id: int | None = None
    Esp_Desc: str | None = None

    Ciu_Cod: str | None = None
    Ciu_Desc: str | None = None

    Dep_Id: str | None = None
    Dep_Desc: str | None = None

    Reg_Id: int | None = None
    Reg_Desc: str | None = None

    Pais_Id: int
    Pais_Desc: str | None = None

    class Config:
        from_attributes = True
