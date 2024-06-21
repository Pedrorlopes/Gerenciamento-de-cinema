from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    duracao = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    estoque = Column(Integer, nullable=False)

    reservas = relationship('Reserva', back_populates='filme')
    sessoes = relationship('Sessao', back_populates='filme')
