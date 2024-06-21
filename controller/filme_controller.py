from services.filme_service import FilmeService

class FilmeController:
    def __init__(self, db_session):
        self.filme_service = FilmeService(db_session)

    def adicionar_filme(self, filme):
        return self.filme_service.adicionar_filme(filme)
