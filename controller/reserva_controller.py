from services.reserva_service import ReservaService

class ReservaController:
    def __init__(self, db_session):
        self.reserva_service = ReservaService(db_session)

    def criar_reserva(self, reserva):
        return self.reserva_service.criar_reserva(reserva)
