from tela.tela_principal import TelaPrincipal
from controle.controle_jogador import ControleJogador
from controle.controle_sessao import ControleSessao


class ControlePrincipal:

    def __init__(self):
        self.__controle_jogador = ControleJogador(self)
        self.__controle_sessao = ControleSessao(self)
        self.__tela_principal = TelaPrincipal
