from sqlalchemy import Column, Integer, String
from app.db.session import Base  # ✅ Cambiado aquí

class Proyecto(Base):
    __tablename__ = "Proyectos"

    Id = Column(String, primary_key=True, index=True)

    ProyTbl_Id = Column(Integer, nullable=True)
    Proy_Id = Column(String, nullable=True)
    Proy_Titulo = Column(String, nullable=True)
    Proy_Desc = Column(String, nullable=True)

    Esp_Id = Column(Integer, nullable=True)
    Esp_Desc = Column(String, nullable=True)

    Cad_Id = Column(Integer, nullable=True)
    Cad_Desc = Column(String, nullable=True)

    Ciu_Id = Column(Integer, nullable=True)
    Ciu_Desc = Column(String, nullable=True)

    Dep_Id = Column(Integer, nullable=True)
    Dep_Desc = Column(String, nullable=True)

    Reg_Id = Column(Integer, nullable=True)
    Reg_Desc = Column(String, nullable=True)

    Pais_Id = Column(Integer, nullable=True)
    Pais_Desc = Column(String, nullable=True)
