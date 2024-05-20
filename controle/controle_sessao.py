import datetime

from tela.tela_sessao import TelaSessao
from entidade.Sessao import Sessao


class ControleSessao:
    def __init__(self, controle_principal):
        self.__controle_principal = controle_principal
        self.__tela_sessao = TelaSessao
        self.__lista_registros = []

    def registrar_sessao(self):
        obter_data = self.__tela_sessao.obter_data_sessao()
        data_sessao = datetime.datetime(obter_data["ano"], obter_data["mes"], obter_data["dia"], obter_data["hora"])

        lista_de_jogadores_participantes = []
        self.__tela_sessao.mostrar_mensagem("Insira os jogadores participantes (insira 0 para terminar)")
        continua = True
        while continua:
            jogador = self.__controle_principal.controle_jogador.selecionar_jogador()
            if jogador is not 0:
                lista_de_jogadores_participantes.append(jogador)
            else:
                continua = not continua

        lista_de_personagens_participantes = []
        '''
        self.__tela_sessao.mostrar_mensagem("Insira os personagens participantes (insira 0 para terminar)")
        continua = True
        while continua:
            personagem = self.__controle_principal.controle_personagem.selecionar_personagem()
        '''
        sessao = Sessao(data_sessao, lista_de_jogadores_participantes, lista_de_personagens_participantes)
        self.__lista_registros.append(sessao)

    def busca_sessao_por_data(self, ano: int, mes: int, dia: int, hora: int):
        dados = datetime.datetime(ano, mes, dia, hora)
        for sessao in self.__lista_registros:
            if sessao.data == dados:
                return sessao
            else:
                return None

    def listar_sessoes(self):
        for sessao in self.__lista_registros:
            self.__tela_sessao.mostrar_sessao({
                "data": sessao.data,
                "jogadores": sessao.lista_jogadores,
                "personagens": sessao.personagens_participantes

            })

    def editar_sessao(self):
        self.__tela_sessao.mostrar_mensagem("Selecione uma sessão para editar inserindo sua data correspondente")
        self.listar_sessoes()
        dados = self.__tela_sessao.obter_data_sessao()
        sessao_editada = self.busca_sessao_por_data(dados["ano"], dados["mes"], dados["dia"], dados["hora"])

        if sessao_editada is not None:
            escolha = self.__tela_sessao.selecionar_edicao()

            if escolha == 1:
                dados = self.__tela_sessao.obter_data_sessao()
                nova_data = datetime.datetime(dados["ano"], dados["ano"], dados["ano"], dados["ano"])
                sessao_editada.data = nova_data

            elif escolha == 2:
                self.__tela_sessao.mostrar_mensagem("Digite o nome do jogador")
                nome = input()
                jogador = self.__controle_principal.controle_jogador.busca_jogador_por_nome(nome)
                if jogador is not None:
                    operacao = self.__tela_sessao.selecionar_operacao()
                    if operacao == 1:
                        sessao_editada.lista_de_jogadores.append(jogador)
                    elif operacao == 2:
                        sessao_editada.lista_de_jogadores.remove(jogador)
                    else:
                        self.__tela_sessao.mostrar_mensagem("Digite o nome do jogador")
                        self.__controle_principal.controle_jogador.busca_jogador_por_nome(nome)
                else:
                    self.__tela_sessao.mostrar_mensagem("Jogador não faz parte da sessão")

            elif escolha == 3:
                ''''''
            else:
                self.__tela_sessao.selecionar_edicao()
        else:
            self.__tela_sessao.mostrar_mensagem("Sessão não cadastrada")

    def excluir_sessao(self):
        self.__tela_sessao.mostrar_mensagem("Selecione uma sessão para excluir inserindo sua data correspondente")
        self.listar_sessoes()
        dados = self.__tela_sessao.obter_data_sessao()
        sessao_excluida = self.busca_sessao_por_data(dados["ano"], dados["mes"], dados["dia"], dados["hora"])
        if sessao_excluida is not None:
            self.__lista_registros.remove(sessao_excluida)
        else:
            self.__tela_sessao.mostrar_mensagem("sessão nao cadastrada")

    def retornar(self):
        self.__controle_principal.abre_tela()

    def mostrar_tela(self):
        lista_opcoes = {
            1: self.registrar_sessao(),
            2: self.editar_sessao(),
            3: self.listar_sessoes(),
            4: self.excluir_sessao(),
            0: self.retornar
        }
        tela_ativa = True
        while tela_ativa:
            lista_opcoes[self.__tela_sessao.tela_opcoes()]()
