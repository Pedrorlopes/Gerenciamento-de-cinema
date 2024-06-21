from sqlalchemy.orm import Session
from .models import Sala

class SalaService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar_sala(self, sala: Sala):
        self.db_session.add(sala)
        self.db_session.commit()
