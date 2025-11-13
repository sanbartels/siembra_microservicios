from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mssql import VARCHAR
from app.db.session import Base

class Proyecto(Base):
    __tablename__ = "tbl_Proyecto"

    ProyTbl_Id = Column(Integer, primary_key=True, autoincrement=False)

    Proy_Id = Column(Integer, nullable=True)
    Proy_Cod = Column(VARCHAR(50), nullable=True)
    Proy_Titulo = Column(String, nullable=True)   # varchar(max)
    Proy_Desc = Column(String, nullable=True)     # varchar(max)

    Esp_Id = Column(Integer, nullable=True)
    Esp_Desc = Column(VARCHAR(200), nullable=True)

    Cad_Id = Column(Integer, nullable=True)
    Cad_Desc = Column(VARCHAR(200), nullable=True)

    Ciu_Cod = Column(VARCHAR(4), nullable=True)
    Ciu_Desc = Column(VARCHAR(150), nullable=True)

    Dep_Id = Column(VARCHAR(6), nullable=True)     # 👈 corregido: era int
    Dep_Desc = Column(VARCHAR(150), nullable=True)

    Reg_Id = Column(Integer, nullable=True)
    Reg_Desc = Column(VARCHAR(100), nullable=True)

    Pais_Id = Column(Integer, nullable=True)
    Pais_Desc = Column(VARCHAR(150), nullable=True)
