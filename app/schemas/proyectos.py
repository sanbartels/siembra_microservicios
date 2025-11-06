from pydantic import BaseModel

class ProyectoBase(BaseModel):
    Id: str
    ProyTbl_Id: int | None = None
    Proy_Id: str | None = None
    Proy_Titulo: str | None = None
    Proy_Desc: str | None = None

    Esp_Id: int | None = None
    Esp_Desc: str | None = None

    Cad_Id: int | None = None
    Cad_Desc: str | None = None

    Ciu_Id: int | None = None
    Ciu_Desc: str | None = None

    Dep_Id: int | None = None
    Dep_Desc: str | None = None

    Reg_Id: int | None = None
    Reg_Desc: str | None = None

    Pais_Id: int | None = None
    Pais_Desc: str | None = None

    class Config:
        from_attributes = True
