from tela.tela_personagem import TelaPersonagem
from controle.controle_inventario import ControleInventario
from entidade.Personagem import Personagem


class ControlePersonagem:
    def __init__(self, controle_principal):
        self.__controle_inventario = ControleInventario(self)
        self.__controle_principal = controle_principal
        self.__tela_personagem = TelaPersonagem()
        self.__personagem = Personagem
        self.__personagens = {}

    # método que irá criar o personagem, assim como criar o inventário dele
    def adicionar_personagem(self):
        # pega os dados do personagem
        dados = self.__tela_personagem.pega_dados_personagem()
        # verifica se o personagem já existe
        if self.__personagens and dados["nome"] in self.__personagens:
            self.__tela_personagem.mostra_mensagem(
                "ERRO! O PERSONAGEM JÁ EXISTE!")
            self.mostra_tela()
        # cria o personagem usando esses dados e o adiciona na lista de
        # personagens
        self.__personagens[dados["nome"]] = self.__personagem(dados["nome"],
                                                              dados["nivel"],
                                                              dados["classe"],
                                                              dados["raça"])
        # cria o inventário do personagem
        self.__personagens[dados["nome"]
                           ].cria_inventario(self.__controle_inventario.cria_inventario())
        self.__tela_personagem.mostra_mensagem(
            f'O personagem {dados["nome"]}'
            ' foi cadastrado com sucesso!')

    # método que remove o personagem
    def remover_personagem(self):
        # verifica se a lista de personagens está vazia, se estiver, avisa
        # o usuário
        if self.__personagens:
            # lista todos os personagens existentes
            self.__tela_personagem.mostra_mensagem(
                '')
            self.listar_personagens()
            # pega o nome do personagem que será removido
            personagem_remover = \
                self.__tela_personagem.remover_personagem()
            # Verifica se o personagem existe na lista de personagens
            # caso exista, ele é removido. Caso contrário, mostra uma
            # mensagem avisando o usuário que não existe um personagem
            # cadastrado com esse nome
            if self.__personagens[personagem_remover]:
                self.__personagens.pop(personagem_remover)
                self.__tela_personagem.mostra_mensagem(
                    f"O personagem {personagem_remover}"
                    " foi excluído com sucesso!")
                return
            self.__tela_personagem.mostra_mensagem(
                "O personagem não existe!")
        else:
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ NENHUM PERSONAGEM CADASTRADO")

    # método que irá atualizar a classe ou o nível de um personagem
    def atualizar_personagem(self):
        # verifica se a lista de personagens está vazia, se estiver, avisa
        # o usuário
        if self.__personagens:
            # lista todos os personagens cadastrados
            self.listar_personagens()
            # pega o nome do personagem que será atualizado
            personagem_atualizar = \
                self.__tela_personagem.pega_nome_personagem()
            # percorre a lista de personagens verificando se existe um
            # personagem com o nome informado pelo usuário
            if self.__personagens[personagem_atualizar]:
                personagem = self.__personagens[personagem_atualizar]
                # pega a informação sobre o que o usuário quer
                # atualizar no personagem
                valor_atualizar = \
                    self.__tela_personagem.opcoes_atualizacao()
                # pega o novo valor para o personagem
                novo_valor = \
                    self.__tela_personagem.pega_dado_atualizacao()
                # verifica se o usuário quer alterar a classe do
                # personagem
                if valor_atualizar == 1:
                    # troca a classe do personagem e avisa o usuário
                    personagem.classe = novo_valor
                    self.__tela_personagem.mostra_mensagem(
                        "A classe do personagem foi"
                        f" alterada para: {personagem.classe}")
                # verifica se o personagem quer atualizar o nível do
                # personagem
                elif valor_atualizar == 2:
                    # calcula quantos níveis o personagem subiu
                    qt_niveis_subidos = novo_valor - personagem.nivel
                    if qt_niveis_subidos <= personagem.nivel:
                        self.__tela_personagem.mostra_mensagem(
                            "ERRO! O NOVO NÍVEL NÃO PODE SER MENOR"
                            " OU IGUAL AO NÍVEL ATUAL!")
                        self.mostra_tela()
                        # atualiza o nível do personagem
                        personagem.nivel = novo_valor
                        # atualiza a variavel que é utilizada ao gerar
                        # o relatório, indicando quantos níveis o
                        # personagem aumentou
                        personagem.qt_niveis_adquiridos = \
                            qt_niveis_subidos
                        self.__tela_personagem.mostra_mensagem(
                            "O personagem aumentou o seu "
                            f"nível para {novo_valor}!")
                    return
            self.__tela_personagem.mostra_mensagem(
                "O personagem não existe!")
        else:
            self.__tela_personagem.mostra_mensagem(
                "Não há nenhum personagem cadastrado")

    # método que lista todos os personagens existentes, mostrando para o
    # usuário
    def listar_personagens(self):
        if self.__personagens:
            self.__tela_personagem.mostra_mensagem("PERSONAGENS ATUALMENTE CADASTRADOS:")
            for personagem in self.__personagens.values():
                self.__tela_personagem.listar_personagens(personagem.nome)
            self.__tela_personagem.mostra_mensagem('')
        else:
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ PERSONAGENS CADASTRADOS!")

    # método que gera um relatório para um determinado personagem,
    # informando quantos níveis ele subiu, quais itens ele adquiriu e
    # quais itens ele perdeu
    def gerar_relatorio(self):
        # verifica se a lista de personagens está vazia
        if self.__personagens:
            # lista os personagens cadastrados
            self.listar_personagens()
            # faz o usuário escolher um personagem para gerar o relatório
            personagem_relatorio = \
                self.__tela_personagem.pega_nome_personagem()
            if self.__personagens[personagem_relatorio]:
                personagem = self.__personagens[personagem_relatorio]
                # pega os itens que o personagem informado ganhou e
                # perdeu
                novos_itens = \
                    [self.__personagens[personagem_relatorio].itens_adquiridos,
                     self.__personagens[personagem_relatorio].itens_perdidos]
                # pega quantos níveis o personagem aumentou
                niveis_adquiridos = personagem.qt_niveis_adquiridos
                # define os itens adquiridos
                itens_adquiridos = novos_itens[0]
                # define os itens perdidos
                itens_perdidos = novos_itens[1]
                # passa os parâmetros para a tela fazer o relatório
                self.__tela_personagem.mostra_relatorio({
                    'Niveis': niveis_adquiridos,
                    'Itens Adquiridos': itens_adquiridos,
                    'Itens Perdidos': itens_perdidos
                })
                return
            self.__tela_personagem.mostra_mensagem(
                "ERRO! O PERSONAGEM INFORMADO NÃO ESTÁ CADASTRADO!")
        else:
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ PERSONAGENS CADASTRADOS!")

    # método que acessa o inventário de um personagem
    def acessar_inventario(self):
        # verifica se a lista de personagens está vazia
        if self.__personagens:
            self.listar_personagens()
            # pega o nome do personagem que será acessado o inventário
            dono_inventario = \
                self.__tela_personagem.pega_nome_personagem()
            # verifica se esse personagem existe
            if self.__personagens[dono_inventario]:
                # informa o controle_inventario qual personagem que
                # estará utilizando o inventário
                self.__controle_inventario. \
                    atualizar_personagem_inventario(dono_inventario)
                # abre a tela do inventário
                self.__controle_inventario.mostra_tela()
            self.__tela_personagem.mostra_mensagem(
                "ERRO! ESSE PERSONAGEM NÃO EXISTE!")
        else:
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ NENHUM PERSONAGEM CADASTRADO,"
                " LOGO, NÃO É POSSÍVEL ACESSAR O INVENTÁRIO!")

    # método usado pelo controle_personagem para cadastrar um
    # personagem de um jogador
    def selecionar_personagem(self):
        if self.__personagens:
            self.listar_personagens()
            nome = self.__tela_personagem.pega_nome_personagem()
            for personagem in self.__personagens:
                if nome == personagem.nome:
                    return personagem
                elif nome == "0":
                    return 0
            self.__tela_personagem.mostra_mensagem(
                "Personagem não existe")
        else:
            self.__tela_personagem.mostra_mensagem(
                "Não há personagens cadastrados")

    def retorna_personagem(self, personagem):
        return self.__personagens[personagem]

    # volta para o controlador principal
    def retornar(self):
        self.__controle_principal.mostrar_tela()

    # controla qual método será utilizado baseado na escolha do usuário
    def mostra_tela(self):
        opcoes = {1: self.adicionar_personagem,
                  2: self.remover_personagem,
                  3: self.listar_personagens,
                  4: self.atualizar_personagem,
                  5: self.acessar_inventario,
                  6: self.gerar_relatorio,
                  0: self.retornar
                  }
        while True:
            opcoes[self.__tela_personagem.tela_opcoes()]()
            self.__tela_personagem.mostra_mensagem('')
