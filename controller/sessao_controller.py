from services.sessao_service import SessaoService

class SessaoController:
    def __init__(self, db_session):
        self.sessao_service = SessaoService(db_session)

    def adicionar_sessao(self, sessao):
        return self.sessao_service.adicionar_sessao(sessao)
