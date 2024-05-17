from controle.controle_principal import ControlePrincipal
from tela.tela_personagem import TelaPersonagem
from entidade.Personagem import Personagem


class ControlePersonagem:
    def __init__(self, controle_principal: ControlePrincipal = '', controle_inventario = ''):
        self.__controle_inventario = controle_inventario
        self.__controle_principal = controle_principal
        self.__tela_personagem = TelaPersonagem()
        self.__personagem = Personagem

    def pega_personagems(self):
        return #self.__controle_principal.controle_personagem.personagens

    def adicionar_personagem(self):
        dados = self.__tela_personagem.pega_dados_personagem()
        personagem = self.__personagem(dados["nome"], dados["nivel"],
                          dados["classe"], dados["raça"])

    def remover_personagem(self):
        personagem = self.__tela_personagem.remover_personagem()
        #ver como está na classe personagem
        #por exemplo, self.__controle_principal.controle_personagem.personagens["Nome"].remove(personagem)

    def atualizar_personagem(self):
        personagem = self.__tela_personagem.pega_nome_personagem()
        novo_valor = self.__tela_personagem.pega_dado_atualizacao()
        #if self.__controle_principal.controle_personagem.personagens[personagem]:
            #self.__controle_principal.controle_personagem.personagens[personagem].valor = novo_valor

    def listar_personagens(self):
        #self.__tela_personagem.listar_personagens(self.pega_personagems())
        pass

    def gerar_relatorio(self):
        personagem = self.__tela_personagem.pega_nome_personagem()
        novos_itens = self.__controle_inventario.pega_itens_relatorio()
        #self.pega_personagem[personagem].nivel
        #self.mostra_mensagem("mensagem aqui")

    def acessar_inventario(self):
        self.__controle_inventario.mostra_tela()

    def mostra_tela(self):
        opcoes = {1: self.adicionar_personagem,
                  2: self.remover_personagem,
                  3: self.listar_personagens,
                  4: self.atualizar_personagem,
                  5: self.acessar_inventario,
                  6: self.gerar_relatorio,
                  0: self.__controle_principal.abre_tela
                  }
        while True:
            opcoes[self.__tela_personagem.tela_opcoes()]()
            self.__tela_personagem.mostra_mensagem('')
