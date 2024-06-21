from services.cliente_service import ClienteService

class ClienteController:
    def __init__(self, db_session):
        self.cliente_service = ClienteService(db_session)

    def adicionar_cliente(self, cliente):
        return self.cliente_service.adicionar_cliente(cliente)
