import datetime
from tela.tela_sessao import TelaSessao
from entidade.Sessao import Sessao
from persistencia.sessao_dao import SessaoDAO
from persistencia.jogador_dao import JogadorDAO


class ControleSessao:
    def __init__(self, controle_principal):
        self.__controle_principal = controle_principal
        self.__tela_sessao = TelaSessao()
        self.__sessao_dao = SessaoDAO()
        self.__jogador_dao = JogadorDAO()
        self.__sessao_selecionado = "vazio"

    def registrar_sessao(self):
        ano, mes, dia, hora = ("1900", "1", "1", "12")
        botao, obter_data = self.__tela_sessao.obter_data_sessao()
        if botao == "Cancel":
            self.retornar()
            ano = int(obter_data["ano"])
            mes = int(obter_data["mes"])
            dia = int(obter_data["dia"])
            hora = int(obter_data["hora"])
        data_sessao = f'{dia}/{mes}/{ano}_{hora}h'

        lista_de_jogadores_participantes = []

        while True:
            botao, valores = self.__controle_principal.controle_jogador.tela_com_todos()
            if botao == "Finalizar":
                break
            else:
                lista_de_jogadores_participantes.append(self.__controle_principal.controle_jogador.jogador_selecionado)
        print(lista_de_jogadores_participantes)

        lista_de_personagens_participantes = self.__controle_principal.controle_personagem.selecionar_personagem()
        print(lista_de_personagens_participantes)

        sessao = Sessao(data_sessao, lista_de_jogadores_participantes,
                        lista_de_personagens_participantes)
        self.__sessao_dao.add(sessao)
        self.mostrar_tela()

    def busca_sessao_por_data(self, ano: int, mes: int, dia: int, hora: int):
        if self.__sessao_dao.get_all():
            dados = datetime.datetime(ano, mes, dia, hora)
            for sessao in self.__sessao_dao.get_all():
                if sessao.data == dados:
                    return sessao
                else:
                    return None
        else:
            self.__tela_sessao.mostrar_mensagem("Não há sessões cadastradas!")

    def listar_sessoes(self):
        if self.__sessao_dao.get_all():
            for sessao in self.__sessao_dao.get_all():
                self.__tela_sessao.mostrar_sessao({
                    "data": sessao.data,
                    "jogadores": sessao.lista_jogadores,
                    "personagens": sessao.personagens_participantes

                })
        else:
            self.__tela_sessao.mostrar_mensagem("Não há sessões cadastradas!")

    def editar_sessao(self):
        if self.__sessao_dao.get_all():
            self.__tela_sessao.mostrar_mensagem("Selecione uma sessão para"
                                                " editar inserindo sua "
                                                "data correspondente")
            self.listar_sessoes()
            dados = self.__tela_sessao.obter_data_sessao()
            sessao_editada = self.busca_sessao_por_data(dados["ano"], dados["mes"],
                                                        dados["dia"], dados["hora"])

            if sessao_editada is not None:
                escolha = self.__tela_sessao.selecionar_edicao()

                if escolha == 1:
                    dados = self.__tela_sessao.obter_data_sessao()
                    nova_data = datetime.datetime(dados["ano"], dados["ano"],
                                                  dados["ano"], dados["ano"])
                    sessao_editada.data = nova_data

                elif escolha == 2:
                    nome = self.__tela_sessao.pega_nome_jogador()
                    jogador = self.__controle_principal.controle_jogador. \
                        busca_jogador_por_nome(nome)
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
                    personagem = self.__controle_principal. \
                        controle_personagem.selecionar_personagem()
                    if personagem in sessao_editada.personagens_participantes:
                        self.__tela_sessao.mostrar_sessao(
                            "Deseja excluir este personagem da sessão?")
                        if self.__tela_sessao.entrada_sim_ou_nao() == "sim":
                            sessao_editada.personagens_participante.remove(personagem)
                        else:
                            self.__tela_sessao.selecionar_edicao()
                    else:
                        self.__tela_sessao.mostrar_mensagem("Deseja adicionar este personagem?")
                        if self.__tela_sessao.entrada_sim_ou_nao() == "sim":
                            sessao_editada.personagens_participante.append(personagem)
                        else:
                            self.__tela_sessao.selecionar_edicao()
                else:
                    self.__tela_sessao.selecionar_edicao()
        else:
            self.__tela_sessao.mostrar_mensagem("Não há sessões cadastradas")

    def excluir_sessao(self):
        if self.__sessao_dao.get_all():
            self.__tela_sessao.mostrar_mensagem(
                "Selecione uma sessão para excluir inserindo sua data "
                "correspondente")
            self.listar_sessoes()
            dados = self.__tela_sessao.obter_data_sessao()
            sessao_excluida = self.busca_sessao_por_data(dados["ano"], dados["mes"],
                                                         dados["dia"], dados["hora"])
            if sessao_excluida is not None:
                self.__sessao_dao.remove(sessao_excluida)
                self.mostrar_tela()
        else:
            self.__tela_sessao.mostrar_mensagem("sessão nao cadastrada")

    def retornar(self):
        self.__controle_principal.mostrar_tela()

    def mostrar_tela(self):
        lista_opcoes = {
            1: self.registrar_sessao,
            2: self.editar_sessao,
            3: self.listar_sessoes,
            4: self.excluir_sessao,
            0: self.retornar
        }
        retorno_da_tela = self.__tela_sessao.tela_opcoes(self.__sessao_dao.listagem())
        try:
            indice_selecionado = (retorno_da_tela[1])[0]
        except IndexError:
            indice_selecionado = 0
        except TypeError:
            indice_selecionado = 0
        try:
            self.__sessao_selecionado = self.__sessao_dao.listagem()[indice_selecionado][0]
        except IndexError:
            self.__sessao_selecionado = 0
        except TypeError:
            self.__sessao_selecionado = 0
        funcao_escolhida = lista_opcoes[retorno_da_tela[0]]
        funcao_escolhida()
