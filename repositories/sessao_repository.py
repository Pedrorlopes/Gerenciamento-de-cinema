from .base_repository import BaseRepository
from models.sessao import Sessao

class SessaoRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
