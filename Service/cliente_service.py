from sqlalchemy.orm import Session
from .models import Cliente

class ClienteService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar_cliente(self, cliente: Cliente):
        self.db_session.add(cliente)
        self.db_session.commit()
