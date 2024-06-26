from persistencia.dao import DAO
from entidade.Sessao import Sessao


class SessaoDAO(DAO):
    def __init__(self):
        super().__init__("sessoes.pkl")

    def add(self, sessao: Sessao, **kwargs):
        if isinstance(sessao, Sessao):
            super().add(sessao.data, sessao)

    def remove(self, sessao: Sessao):
        if isinstance(sessao, Sessao):
            self.remove(sessao.data)
