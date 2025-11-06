from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Oferta(Base):
    __tablename__ = "tbl_Oferta"

    OferTbl_Id = Column(Integer, primary_key=True, index=True)
    Ofer_Id = Column(Integer, nullable=False)
    Ofer_Titulo = Column(String(5000))
    Ofer_Desc = Column(String)
    Esp_Id = Column(Integer)
    Esp_Desc = Column(String(500))
    Cad_Id = Column(Integer)
    Cad_Desc = Column(String(500))
    Ciu_Cod = Column(String(4))
    Ciu_Desc = Column(String(150))
    Dep_Id = Column(String(6))
    Dep_Desc = Column(String(150))
    Reg_Id = Column(Integer)
    Reg_Desc = Column(String(150))
    Pais_Id = Column(Integer)
    Pais_Desc = Column(String(500))
