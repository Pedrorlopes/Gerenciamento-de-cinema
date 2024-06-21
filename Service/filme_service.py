from sqlalchemy.orm import Session
from .models import Filme

class FilmeService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar_filme(self, filme: Filme):
        self.db_session.add(filme)
        self.db_session.commit()
