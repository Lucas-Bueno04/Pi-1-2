from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.model.settings.base import Base

class Rodada(Base):
    __tablename__ = 'rodada'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pontuacao = Column(Integer, nullable=False)
    data = Column(Date, nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)

    # Relacionamento
    usuario = relationship("Usuario", back_populates="rodadas")