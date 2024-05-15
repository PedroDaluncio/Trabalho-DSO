from tela.tela_sessao import TelaSessao
from entidade.sessao import Sessao


class ControleSessao:
    def __init__(self, controle_principal):
        self.__controle_principal = controle_principal
        self.__tela_sessao = TelaSessao
        self.__lista_registros = []

    def registrar_sessao(self):
        dados_sesao = self.__tela_sessao.obter_dados_sessao()
