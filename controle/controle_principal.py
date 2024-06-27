from controle.controle_personagem import ControlePersonagem
from tela.tela_principal import TelaPrincipal
from controle.controle_jogador import ControleJogador
from controle.controle_sessao import ControleSessao


class ControlePrincipal:

    def __init__(self):
        self.__controle_jogador = ControleJogador(self)
        self.__controle_sessao = ControleSessao(self)
        self.__controle_personagem = ControlePersonagem(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def controle_jogador(self):
        return self.__controle_jogador

    @property
    def controle_sessao(self):
        return self.__controle_sessao

    @property
    def controle_personagem(self):
        return self.__controle_personagem

    def cadastra_jogador(self):
        self.__controle_jogador.mostrar_tela()

    def cadastra_personagem(self):
        self.__controle_personagem.mostra_tela()

    def cadastra_sessao(self):
        self.__controle_sessao.mostrar_tela()

    def encerra_sistema(self):
        exit(0)

    def mostrar_tela(self):
        lista_opcoes = {
            1: self.cadastra_jogador,
            2: self.cadastra_personagem,
            3: self.cadastra_sessao,
            0: self.encerra_sistema
        }
        opcao_escolhida = self.__tela_principal.tela_opcoes()
        lista_opcoes[opcao_escolhida]()

    def inicializa_sistema(self):
        self.mostrar_tela()
