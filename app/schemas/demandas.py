from pydantic import BaseModel

class DemandaBase(BaseModel):
    DemTbl_Id: int
    Dem_Id: int | None = None
    Dem_Titulo: str | None = None
    Dem_Desc: str | None = None

    Reg_Id: int | None = None
    Reg_Desc: str | None = None

    Dep_Id: str | None = None
    Dep_Desc: str | None = None

    Esp_Id: int
    Esp_Desc: str | None = None

    class Config:
        from_attributes = True
