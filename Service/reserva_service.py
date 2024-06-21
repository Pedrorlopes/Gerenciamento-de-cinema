from sqlalchemy.orm import Session
from .models import Reserva

class ReservaService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def criar_reserva(self, reserva: Reserva):
        self.db_session.add(reserva)
        self.db_session.commit()
