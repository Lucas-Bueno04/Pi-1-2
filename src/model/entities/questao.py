from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.model.settings.base import Base

class Questao(Base):
    __tablename__ = 'questao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    enunciado = Column(Text, nullable=False)
    materia = Column(String(50),nullable=False )
    dica = Column(Text)

    # Relacionamento
    alternativas = relationship("Alternativa", back_populates="questao")