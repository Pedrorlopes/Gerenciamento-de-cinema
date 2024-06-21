from services.cinema_service import CinemaService

class CinemaController:
    def __init__(self, db_session):
        self.cinema_service = CinemaService(db_session)

    def vender_ingresso(self, sessao_id, cliente, nota_avaliacao):
        return self.cinema_service.vender_ingresso(sessao_id, cliente, nota_avaliacao)
