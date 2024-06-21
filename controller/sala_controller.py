from services.sala_service import SalaService

class SalaController:
    def __init__(self, db_session):
        self.sala_service = SalaService(db_session)

    def adicionar_sala(self, sala):
        return self.sala_service.adicionar_sala(sala)
