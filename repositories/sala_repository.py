from .base_repository import BaseRepository
from models.sala import Sala

class SalaRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
