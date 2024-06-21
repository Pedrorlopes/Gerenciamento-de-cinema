from sqlalchemy.orm import Session
from datetime import datetime
from .models import Sessao, Reserva

class CinemaService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def vender_ingresso(self, sessao_id, cliente, nota_avaliacao):
        sessao = self.db_session.query(Sessao).filter_by(id=sessao_id).first()
        if sessao:
            filme = sessao.filme
            if filme.estoque > 0:
                if 0 <= nota_avaliacao <= 10:
                    reserva = Reserva(filme=filme, cliente=cliente, sessao=sessao, nota_avaliacao=nota_avaliacao)
                    filme.estoque -= 1
                    self.db_session.add(reserva)
                    self.db_session.commit()
                    print(f"Ingresso vendido para {cliente.nome} para o filme {filme.titulo} na sessão {sessao.horario}.")
                else:
                    print("A nota de avaliação deve estar entre 0 e 10.")
            else:
                print(f"Desculpe, {filme.titulo} está fora de estoque.")
        else:
            print(f"Desculpe, a sessão com ID {sessao_id} não está disponível.")
