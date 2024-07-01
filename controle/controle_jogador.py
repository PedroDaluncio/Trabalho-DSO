from tela.tela_jogador import TelaJogador
from entidade.Jogador import Jogador
from persistencia.jogador_dao import JogadorDAO


class ControleJogador:
    def __init__(self, controle_principal):
        self.__controle_principal = controle_principal
        self.__tela_jogador = TelaJogador()
        self.__jogador = Jogador
        self.__jogador_dao = JogadorDAO()
        self.__jogador_selecionado = "vazio"

    @property
    def jogador_selecionado(self):
        return self.__jogador_selecionado

    @jogador_selecionado.setter
    def jogador_selecionado(self, jogador_selecionado):
        self.__jogador_selecionado = jogador_selecionado

    def busca_jogador_por_nome(self, nome: str):
        for jogador in self.__jogador_dao.get_all():
            if jogador.nome == nome:
                return jogador
            elif nome == "0":
                return 0
            return None

    def adicionar_jogador(self):
        dados_jogador = self.__tela_jogador.pega_dados_jogador()
        validacao = self.busca_jogador_por_nome(dados_jogador["nome"])
        if validacao is None:
            jogador = self.__jogador(dados_jogador["nome"], dados_jogador["idade"])
            self.__jogador_dao.add(jogador)
            self.mostrar_tela()
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador já cadastrado")

    def atribuir_personagem(self):
        if self.__jogador_dao.get_all():
            objeto = self.__jogador_dao.seleciona_um(self.jogador_selecionado)
            personagem = self.__controle_principal.controle_personagem.selecionar_personagem()
        else:
            self.__tela_jogador.mostrar_mensagem("Não há jogadores cadastrados")
            self.mostrar_tela()
        self.mostrar_tela()

    def editar_jogador(self):
        if self.__jogador_dao.get_all():
            objeto = self.__jogador_dao.seleciona_um(self.jogador_selecionado)
            escolha = (self.__tela_jogador.tela_com_dois_botoes
                       ("Escolha o que deseja alterar", "Nome", "Idade"))
            if escolha == 1:
                novo_nome = self.__tela_jogador.tela_de_input("Digite o novo nome")
                objeto.nome = novo_nome
            elif escolha == 2:
                nova_idade = self.__tela_jogador.tela_de_input("Digite uma nova idade")
                objeto.idade = nova_idade
            self.__jogador_dao.save()
            self.mostrar_tela()
        else:
            self.__tela_jogador.mostrar_mensagem("Não há jogadores cadastrado")
            self.mostrar_tela()

    def excluir_jogador(self):
        if self.__jogador_dao.get_all():
            escolha = (self.__tela_jogador.tela_com_dois_botoes
                       ("Deseja mesmo excluir?", "Sim", "Não"))
            if escolha == 1:
                self.__jogador_dao.remove(self.__jogador_selecionado)
                self.mostrar_tela()
            elif escolha == 2:
                self.mostrar_tela()
        else:
            self.__tela_jogador.mostrar_mensagem("Não há jogadores cadastrados")
            self.mostrar_tela()

    def retornar(self):
        self.__controle_principal.mostrar_tela()

    def mostrar_tela(self):
        lista_opcoes = {
            1: self.adicionar_jogador,
            2: self.editar_jogador,
            4: self.excluir_jogador,
            5: self.atribuir_personagem,
            0: self.retornar
        }
        button, indice_selecionado = self.__tela_jogador.tela_opcoes(self.__jogador_dao.listagem())
        if not indice_selecionado:
            indice_selecionado = [0]
        indice = indice_selecionado[0]
        print(indice)
        try:
            self.__jogador_selecionado = self.__jogador_dao.listagem()[indice][0]
        except IndexError:
            self.__jogador_selecionado = "Vazio"
        funcao_escolhida = lista_opcoes[button]
        funcao_escolhida()

    def tela_com_todos(self):
        button, indice_selecionado = self.__tela_jogador.tela_com_todos(self.__jogador_dao.listagem())
        if not indice_selecionado:
            indice_selecionado = [0]
        indice = indice_selecionado[0]
        print(indice)
        try:
            self.__jogador_selecionado = self.__jogador_dao.listagem()[indice][0]
        except IndexError:
            self.__jogador_selecionado = "Vazio"
        return button, indice_selecionado
