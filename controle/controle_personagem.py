from tela.tela_personagem import TelaPersonagem
from controle.controle_inventario import ControleInventario
from entidade.Personagem import Personagem
from persistencia.personagem_dao import PersonagemDAO
from tratamento_excesoes.excecao_close import JanelaFechadaException


class ControlePersonagem:
    def __init__(self, controle_principal):
        self.__controle_inventario = ControleInventario(self)
        self.__controle_principal = controle_principal
        self.__tela_personagem = TelaPersonagem()
        self.__personagem = Personagem
        self.__personagens = PersonagemDAO()

    # método que irá criar o personagem, assim como criar o inventário dele
    def adicionar_personagem(self):
        try:
            # pega os dados do personagem
            dados = self.__tela_personagem.pega_dados_personagem()
            if dados == 'ação interrompida':
                raise JanelaFechadaException()
            # verifica se o personagem já existe
            if self.__personagens.get_all() and (dados["nome"] == personagem.nome for personagem in self.__personagens.get_all()):
                self.__tela_personagem.mostra_mensagem(
                    "ERRO! O PERSONAGEM JÁ EXISTE!")
                self.mostra_tela()
            # cria o personagem usando esses dados e o adiciona na lista de
            # personagens
            personagem = self.__personagem(dados["nome"], dados["nivel"], dados["classe"], dados["raça"])
            personagem.cria_inventario(self.__controle_inventario.cria_inventario())
            self.__personagens.add(personagem)
            self.__tela_personagem.mostra_mensagem(
                f'O personagem {dados["nome"]}'
                ' foi cadastrado com sucesso!')
        except JanelaFechadaException:
            self.mostra_tela()

    # método que remove o personagem
    def remover_personagem(self):
        try:
            # verifica se a lista de personagens está vazia, se estiver, avisa
            # o usuário
            if self.__personagens.get_all():
                lista_personagens = []
                for personagem in self.__personagens.get_all():
                    lista_personagens.append(personagem.nome)
                # pega o nome do personagem que será removido
                personagem_remover = \
                    self.__tela_personagem.remover_personagem(
                        lista_personagens)
                if personagem_remover == 'ação interrompida':
                    raise JanelaFechadaException()
                # Verifica se o personagem existe na lista de personagens
                # caso exista, ele é removido. Caso contrário, mostra uma
                # mensagem avisando o usuário que não existe um personagem
                # cadastrado com esse nome
                self.__personagens.remove(personagem_remover)
                self.__tela_personagem.mostra_mensagem(
                    f"O personagem {personagem_remover}"
                    " foi excluído com sucesso!")
                return
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ NENHUM PERSONAGEM CADASTRADO")
        except JanelaFechadaException:
            self.mostra_tela()

    # método que irá atualizar a classe ou o nível de um personagem
    def atualizar_personagem(self):
        try:
            # verifica se a lista de personagens está vazia, se estiver, avisa
            # o usuário
            if self.__personagens.get_all():
                # pega o nome do personagem que será atualizado
                lista_personagens = []
                for personagem in self.__personagens.get_all():
                    lista_personagens.append(personagem.nome)
                personagem_atualizar = \
                    self.__tela_personagem.pega_nome_personagem(
                        lista_personagens)
                # percorre a lista de personagens verificando se existe um
                # personagem com o nome informado pelo usuário
                if self.__personagens.get(personagem_atualizar):
                    personagem = self.__personagens.get(personagem_atualizar)
                    # pega a informação sobre o que o usuário quer
                    # atualizar no personagem
                    valor_atualizar = \
                        self.__tela_personagem.opcoes_atualizacao()
                    if valor_atualizar == 'ação interrompida':
                        raise JanelaFechadaException()
                    # pega o novo valor para o personagem
                    novo_valor = \
                        self.__tela_personagem.pega_dado_atualizacao(
                            valor_atualizar)
                    if novo_valor == 'ação interrompida':
                        raise JanelaFechadaException()
                    # verifica se o usuário quer alterar a classe do
                    # personagem
                    if valor_atualizar == "classe":
                        # troca a classe do personagem e avisa o usuário
                        personagem.classe = novo_valor
                        self.__tela_personagem.mostra_mensagem(
                            "A classe do personagem foi"
                            f" alterada para: {personagem.classe}")
                    # verifica se o personagem quer atualizar o nível do
                    # personagem
                    elif valor_atualizar == "nivel":
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
            else:
                self.__tela_personagem.mostra_mensagem(
                    "Não há nenhum personagem cadastrado")
        except JanelaFechadaException:
            self.mostra_tela()

    # método que lista todos os personagens existentes, mostrando para o
    # usuário
    def listar_personagens(self):
        if self.__personagens.get_all():
            lista_personagens = []
            for personagem in self.__personagens.get_all():
                lista_personagens.append(personagem.nome)
            self.__tela_personagem.listar_personagens(
                lista_personagens)
        else:
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ PERSONAGENS CADASTRADOS!")

    # método que gera um relatório para um determinado personagem,
    # informando quantos níveis ele subiu, quais itens ele adquiriu e
    # quais itens ele perdeu
    def gerar_relatorio(self):
        try:
            # verifica se a lista de personagens está vazia
            if self.__personagens.get_all():
                lista_personagens = []
                for personagem in self.__personagens.get_all():
                    lista_personagens.append(personagem.nome)
                # faz o usuário escolher um personagem para gerar o relatório
                personagem_relatorio = \
                    self.__tela_personagem.pega_nome_personagem(
                        lista_personagens)
                if personagem_relatorio == 'ação interrompida':
                    raise JanelaFechadaException()
                personagem = self.__personagens.get(personagem_relatorio)
                # pega os itens que o personagem informado ganhou e
                # perdeu
                novos_itens = \
                    [self.__personagens.get(personagem_relatorio).itens_adquiridos,
                    self.__personagens.get(personagem_relatorio).itens_perdidos]
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
                self.mostra_tela()
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ PERSONAGENS CADASTRADOS!")
        except JanelaFechadaException:
            self.mostra_tela()

    # método que acessa o inventário de um personagem
    def acessar_inventario(self):
        try:
            # verifica se a lista de personagens está vazia
            if self.__personagens.get_all():
                lista_personagens = []
                for personagem in self.__personagens.get_all():
                    lista_personagens.append(personagem.nome)
                # pega o nome do personagem que será acessado o inventário
                dono_inventario = \
                    self.__tela_personagem.pega_nome_personagem(
                        lista_personagens)
                if dono_inventario == 'ação interrompida':
                    raise JanelaFechadaException()
                # informa o controle_inventario qual personagem que
                # estará utilizando o inventário
                self.__controle_inventario. \
                    atualizar_personagem_inventario(dono_inventario)
                # abre a tela do inventário
                self.__controle_inventario.mostra_tela()
            else:
                self.__tela_personagem.mostra_mensagem(
                    "ERRO! NÃO HÁ NENHUM PERSONAGEM CADASTRADO,"
                    " LOGO, NÃO É POSSÍVEL ACESSAR O INVENTÁRIO!")
        except JanelaFechadaException:
            self.mostra_tela()

    # método usado pelo controle_personagem para cadastrar um
    # personagem de um jogador
    def selecionar_personagem(self):
        try:
            if self.__personagens.get_all():
                lista_personagens = []
                for personagem in self.__personagens.get_all():
                    lista_personagens.append(personagem.nome)
                nome = self.__tela_personagem.pega_nome_personagem(
                    lista_personagens)
                if nome == 'ação interrompida':
                    raise JanelaFechadaException()
                return self.__personagens.get(nome)
            self.__tela_personagem.mostra_mensagem(
                "Não há personagens cadastrados")
        except JanelaFechadaException:
            self.mostra_tela()

    def retorna_personagem(self, personagem):
        return self.__personagens.get(personagem)

    # volta para o controlador principal
    def retornar(self):
        self.__controle_principal.mostrar_tela()

    def atualiza_dao(self, personagem):
        self.__personagens.add(personagem)

    # controla qual método será utilizado baseado na escolha do usuário
    def mostra_tela(self):
        try:
            opcoes = {1: self.adicionar_personagem,
                    2: self.remover_personagem,
                    3: self.listar_personagens,
                    4: self.atualizar_personagem,
                    5: self.acessar_inventario,
                    6: self.gerar_relatorio,
                    0: self.retornar
                    }
            while True:
                opcao_selecionada = self.__tela_personagem.tela_opcoes()
                if opcao_selecionada == 'ação interrompida':
                    raise JanelaFechadaException()
                opcoes[opcao_selecionada]()
        except JanelaFechadaException:
            self.retornar()

