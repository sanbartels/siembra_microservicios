from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Demanda(Base):
    __tablename__ = "tbl_Demanda"

    DemTbl_Id = Column(Integer, primary_key=True, index=True)
    Dem_Id = Column(Integer, nullable=False)
    Dem_Titulo = Column(String(5000))
    Dem_Desc = Column(String(5000))
    Cad_Id = Column(Integer)
    Cad_Desc = Column(String(200))
    Reg_Id = Column(Integer)
    Reg_Desc = Column(String(100))
    Dep_Id = Column(String(2))
    Dep_Desc = Column(String(50))
    Esp_Id = Column(Integer)
    Esp_Desc = Column(String(200))
