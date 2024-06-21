from sqlalchemy.orm import Session
from .models import Sessao

class SessaoService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar_sessao(self, sessao: Sessao):
        self.db_session.add(sessao)
        self.db_session.commit()
