from .base_repository import BaseRepository
from models.filme import Filme

class FilmeRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
