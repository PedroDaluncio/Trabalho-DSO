from tela.tela_jogador import TelaJogador
from entidade.Jogador import Jogador


class ControleJogador:
    def __init__(self, controle_principal):
        self.__controle_principal = controle_principal
        self.__tela_jogador = TelaJogador()
        self.__jogador = Jogador
        self.__lista_de_jogadores = []

    def busca_jogador_por_nome(self, nome: str):
        for jogador in self.__lista_de_jogadores:
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
            self.__lista_de_jogadores.append(jogador)
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador já cadastrado")

    def atribuir_personagem(self):
        if self.__lista_de_jogadores:
            self.listar_jogadores()
            nome_jogador = self.__tela_jogador.seleciona_jogador()
            jogador_selecionado = self.busca_jogador_por_nome(nome_jogador)
            if jogador_selecionado is not None:
                personagem = self.__controle_principal.controle_personagem.selecionar_personagem()
                if personagem.nome not in jogador_selecionado.personagens.keys():
                    jogador_selecionado.personagens[personagem.nome] = personagem
                    self.__tela_jogador.mostrar_mensagem("O personagem "
                                                         f"{personagem.nome}"
                                                         " foi cadastrado ao"
                                                         " jogador "
                                                         f"{nome_jogador}!")
                else:
                    self.__tela_jogador.mostrar_mensagem("Personagem ja pertence a este jogador")
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não cadastrado")

    def editar_jogador(self):
        if self.__lista_de_jogadores:
            self.listar_jogadores()
            nome_jogador = self.__tela_jogador.seleciona_jogador()
            jogador_editado = self.busca_jogador_por_nome(nome_jogador)
            if jogador_editado is not None:
                novos_dados_jogador = self.__tela_jogador.pega_dados_jogador()
                jogador_editado.nome = novos_dados_jogador["nome"]
                jogador_editado.idade = novos_dados_jogador["idade"]
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não cadastrado")

    def listar_jogadores(self):
        if self.__lista_de_jogadores:
            for jogador in self.__lista_de_jogadores:
                self.__tela_jogador.mostra_jogadores({"nome": jogador.nome, "idade": jogador.idade})
        else:
            self.__tela_jogador.mostrar_mensagem("Não há jogadores cadastrados")

    def selecionar_jogador(self):
        if self.__lista_de_jogadores:
            nome_jogador = self.__tela_jogador.seleciona_jogador()
            jogador_selecionado = self.busca_jogador_por_nome(nome_jogador)
            if jogador_selecionado == 0:
                return 0
            elif jogador_selecionado is not None:
                return jogador_selecionado
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não cadastrado")

    def excluir_jogador(self):
        if self.__lista_de_jogadores:
            self.listar_jogadores()
            nome_jogador = self.__tela_jogador.seleciona_jogador()
            nome = self.busca_jogador_por_nome(nome_jogador)
            if nome is not None:
                self.__lista_de_jogadores.remove(nome)
                self.listar_jogadores()
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não cadastrado")

    def retornar(self):
        self.__controle_principal.mostrar_tela()

    def mostrar_tela(self):
        lista_opcoes = {
            1: self.adicionar_jogador,
            2: self.editar_jogador,
            3: self.listar_jogadores,
            4: self.excluir_jogador,
            5: self.atribuir_personagem,
            0: self.retornar
        }
        tela_ativa = True
        while tela_ativa:
            opcao_escolhida = self.__tela_jogador.tela_opcoes()
            funcao_escolhida = lista_opcoes[int(opcao_escolhida)]
            funcao_escolhida()
