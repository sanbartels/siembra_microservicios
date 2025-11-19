from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mssql import VARCHAR
from app.db.session import Base

class Demanda(Base):
    __tablename__ = "tbl_Demanda"

    DemTbl_Id = Column(Integer, primary_key=True, autoincrement=False)
    Dem_Id = Column(Integer, nullable=True)
    Dem_Titulo = Column(String, nullable=True)
    Dem_Desc = Column(String, nullable=True)

    Reg_Id = Column(Integer, nullable=True)
    Reg_Desc = Column(VARCHAR(100), nullable=True)

    Dep_Id = Column(VARCHAR(2), nullable=True)
    Dep_Desc = Column(VARCHAR(50), nullable=True)

    Esp_Id = Column(Integer, nullable=False)
    Esp_Desc = Column(VARCHAR(200), nullable=True)
