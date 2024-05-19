from tela.tela_personagem import TelaPersonagem
from controle.controle_inventario import ControleInventario
from entidade.Personagem import Personagem


class ControlePersonagem:
    def __init__(self, controle_principal = ''):
        self.__controle_inventario = ControleInventario(self)
        self.__controle_principal = controle_principal
        self.__tela_personagem = TelaPersonagem()
        self.__personagem = Personagem
        self.__personagens = []

    def adicionar_personagem(self):
        dados = self.__tela_personagem.pega_dados_personagem()
        self.__personagens.append(self.__personagem(dados["nome"],
                                                    dados["nivel"],
                                                    dados["classe"],
                                                    dados["raça"]))
        self.__controle_inventario.cria_inventario(dados["nome"])
        self.__tela_personagem.mostra_mensagem(
            f'O personagem {dados["nome"]} foi cadastrado com sucesso!')

    def remover_personagem(self):
        if self.__personagens:
            self.__tela_personagem.mostra_mensagem(
                "PERSONAGENS EXISTENTES:")
            self.listar_personagens()
            personagem_remover = \
                self.__tela_personagem.remover_personagem()
            for personagem in self.__personagens:
                if personagem.nome == personagem_remover:
                    self.__personagens.remove(personagem)
                    self.__tela_personagem.mostra_mensagem(
                        f"O personagem {personagem.nome} foi excluído com sucesso!")
                    return
            self.__tela_personagem.mostra_mensagem(
                "O personagem não existe!")
        else:
            self.__tela_personagem.mostra_mensagem(
                "Não há nenhum personagem cadastrado!")

    def atualizar_personagem(self):
        if self.__personagens:
            self.__tela_personagem.mostra_mensagem(
                "PERSONAGENS EXISTENTES:")
            self.listar_personagens()
            personagem_atualizar = \
                self.__tela_personagem.pega_nome_personagem()
            for personagem in self.__personagens:
                if personagem.nome == personagem_atualizar:
                    valor_atualizar = \
                        self.__tela_personagem.opcoes_atualizacao()
                    novo_valor = \
                        self.__tela_personagem.pega_dado_atualizacao()
                    if valor_atualizar == 1:
                        personagem.classe = novo_valor
                        self.__tela_personagem.mostra_mensagem(
                            "A classe do personagem foi"
                            f" alterada para: {personagem.classe}")
                    elif valor_atualizar == 2:
                        novo_valor = int(novo_valor)
                        qt_niveis_subidos = novo_valor - personagem.nivel
                        personagem.nivel = novo_valor
                        personagem.qt_niveis_adquiridos = qt_niveis_subidos
                        self.__tela_personagem.mostra_mensagem(
                            f"O personagem aumentou o seu nível para {novo_valor}!")
                    return
            self.__tela_personagem.mostra_mensagem(
                "O personagem não existe!")
        else:
            self.__tela_personagem.mostra_mensagem(
                "Não há nenhum personagem cadastrado")

    def listar_personagens(self):
        self.__tela_personagem.listar_personagens(self.__personagens)

    def gerar_relatorio(self):
        if self.__personagens:
            personagem_relatorio = self.__tela_personagem.pega_nome_personagem()
            novos_itens = self.__controle_inventario.pega_itens_relatorio()
            for personagem in self.__personagens:
                if personagem.nome == personagem_relatorio:
                    niveis_adquiridos = personagem.qt_niveis_adquiridos
                    itens_adquiridos = novos_itens[0][personagem_relatorio]
                    itens_perdidos = novos_itens[1][personagem_relatorio]
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

    def acessar_inventario(self):
        if self.__personagens:
            self.listar_personagens()
            dono_inventario = input(
                "Deseja acessar o inventário de qual personagem? ")
            for personagem in self.__personagens:
                if personagem.nome == dono_inventario:
                    self.__controle_inventario.atualizar_personagem_inventario(dono_inventario)
                    self.__controle_inventario.mostra_tela()
            self.__tela_personagem.mostra_mensagem(
                "ERRO! ESSE PERSONAGEM NÃO EXISTE!")
        else:
            self.__tela_personagem.mostra_mensagem(
                "ERRO! NÃO HÁ NENHUM PERSONAGEM CADASTRADO,"
                    " LOGO, NÃO É POSSÍVEL ACESSAR O INVENTÁRIO!")

    def perga_personagem_no_inventario(self):
        return self.__personagem.personagem_no_inventario

    def retornar(self):
        self.__controle_principal.abre_tela()

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
            self.__tela_personagem.mostra_mensagem('')
            opcoes[self.__tela_personagem.tela_opcoes()]()
