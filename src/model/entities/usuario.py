from sqlalchemy import Column, Integer, String, Boolean, BLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.model.settings.base import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(BLOB, nullable=False)
    type = Column(Boolean, nullable=False)

    # Relacionamentos
    rodadas = relationship("Rodada", back_populates="usuario")