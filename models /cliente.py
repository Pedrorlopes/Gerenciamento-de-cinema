from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)

    reservas = relationship('Reserva', back_populates='cliente')
