from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Sala(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    capacidade = Column(Integer, nullable=False)

    sessoes = relationship('Sessao', back_populates='sala')

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'capacidade': self.capacidade
        }
