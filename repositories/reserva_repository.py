from .base_repository import BaseRepository
from models.reserva import Reserva

class ReservaRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)
