from .base_repository import BaseRepository
from models.cliente import Cliente

class ClienteRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)

    def get_by_cpf(self, cpf):
        return self.session.query(Cliente).filter(Cliente.cpf == cpf).first()
