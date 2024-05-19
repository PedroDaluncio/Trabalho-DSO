from tela.tela_jogador import TelaJogador
from entidade.jogador import Jogador


class ControleJogador:
    def __init__(self, controle_principal):
        self.__controle_principal = controle_principal
        self.__tela_jogador = TelaJogador
        self.__lista_de_jogadores = []

    def busca_jogador_por_nome(self, nome: str):
        for jogador in self.__lista_de_jogadores:
            if jogador.nome == nome:
                return jogador
            return None

    def adicionar_jogador(self):
        dados_jogador = self.__tela_jogador.pega_dados_jogador()
        validacao = self.busca_jogador_por_nome(dados_jogador["nome"])
        if validacao is None:
            jogador = Jogador(dados_jogador["nome"], dados_jogador["idade"])
            self.__lista_de_jogadores.append(jogador)
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador já cadastrado")

    '''Essa parte fiquei na duvida em como atribuir um personagem ao jogador ou se fazer ao contrário
    
    def atribuir_personagem(self):
        self.listar_jogadores()
        nome_jogador = self.__tela_jogador.seleciona_jogador()
        jogador_selecionado = self.busca_jogador_por_nome(nome_jogador)
        if jogador_selecionado is not None:
            ...
        
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não cadastrado")
    '''
    def editar_jogador(self):
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
        for jogador in self.__lista_de_jogadores:
            self.__tela_jogador.mostra_jogadores({"nome": jogador.nome, "idade": jogador.idade})
        if len(self.__lista_de_jogadores) == 0:
            self.__tela_jogador.mostrar_mensagem("Não há jogadores cadastrados")

    def selecionar_jogador(self):
        nome_jogador = self.__tela_jogador.seleciona_jogador()
        jogador_selecionado = self.busca_jogador_por_nome(nome_jogador)
        if jogador_selecionado is not None:
            return jogador_selecionado
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não cadastrado")


    def excluir_jogador(self):
        self.listar_jogadores()
        nome_jogador = self.__tela_jogador.seleciona_jogador()
        nome = self.busca_jogador_por_nome(nome_jogador)
        if nome is not None:
            self.__lista_de_jogadores.remove(nome)
            self.listar_jogadores()
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não cadastrado")

    def retornar(self):
        self.__controle_principal.abre_tela()

    def mostrar_tela(self):
        lista_opcoes = {
            1: self.adicionar_jogador,
            2: self.editar_jogador,
            3: self.listar_jogadores,
            4: self.excluir_jogador,
            0: self.retornar
        }
        tela_ativa = True
        while tela_ativa:
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()
