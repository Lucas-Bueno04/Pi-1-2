from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.model.settings.base import Base

class Alternativa(Base):
    __tablename__ = 'alterativa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    q_id = Column(Integer, ForeignKey('questao.id'), nullable=False)
    enunciado = Column(Text, nullable=False)
    verify = Column(Boolean, nullable=False)

    # Relacionamento
    questao = relationship("Questao", back_populates="alternativas")