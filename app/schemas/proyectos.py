from pydantic import BaseModel

class ProyectoBase(BaseModel):
    ProyTbl_Id: int
    Proy_Id: int | None = None
    Proy_Cod: str | None = None
    Proy_Titulo: str | None = None
    Proy_Desc: str | None = None

    Esp_Id: int | None = None
    Esp_Desc: str | None = None

    Cad_Id: int | None = None
    Cad_Desc: str | None = None

    Ciu_Cod: str | None = None
    Ciu_Desc: str | None = None

    Dep_Id: str | None = None
    Dep_Desc: str | None = None

    Reg_Id: int | None = None
    Reg_Desc: str | None = None

    Pais_Id: int | None = None
    Pais_Desc: str | None = None

    class Config:
        from_attributes = True
