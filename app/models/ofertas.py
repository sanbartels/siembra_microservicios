from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mssql import VARCHAR
from app.db.session import Base

class Oferta(Base):
    __tablename__ = "tbl_Oferta"

    OferTbl_Id = Column(Integer, primary_key=True, autoincrement=False)
    Ofer_Id = Column(Integer, nullable=True)
    Ofer_Titulo = Column(String, nullable=True)
    Ofer_Desc = Column(String, nullable=True)

    Esp_Id = Column(Integer, nullable=True)
    Esp_Desc = Column(VARCHAR(500), nullable=True)

    Cad_Id = Column(Integer, nullable=True)
    Cad_Desc = Column(VARCHAR(500), nullable=True)

    Ciu_Cod = Column(VARCHAR(4), nullable=True)
    Ciu_Desc = Column(VARCHAR(150), nullable=True)

    Dep_Id = Column(VARCHAR(6), nullable=True)
    Dep_Desc = Column(VARCHAR(150), nullable=True)

    Reg_Id = Column(Integer, nullable=True)
    Reg_Desc = Column(VARCHAR(150), nullable=True)

    Pais_Id = Column(Integer, nullable=False)
    Pais_Desc = Column(VARCHAR(500), nullable=True)
