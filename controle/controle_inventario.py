from controle_personagem import ControlePersonagem
from tela.tela_inventario import TelaInventario
from entidade.inventario import Inventario
from outras_classes.arremesavel import Arremesavel
from outras_classes.consumivel import Consumivel
from outras_classes.equipavel import Equipavel


class ControleInventario:
    def __init__(self, controle_personagem: ControlePersonagem):
        self.__tela_inventario = TelaInventario()
        self.__entidade_inventario = Inventario()
        self.__controle_personagem = ControlePersonagem()

    def adicionar_consumivel(self, consumivel):
        if isinstance(consumivel, Consumivel):
            self.__entidade_inventario.espaco_interno(consumivel)
            self.__tela_inventario.mostra_mensagem(
                f"O item {consumivel.nome} foi adicionado ao inventário!")
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Insira um consumível válido!")

    def adicionar_arremesavel(self, arremesavel):
        if isinstance(arremesavel, Arremesavel):
            self.__entidade_inventario.espaco_interno(arremesavel)
            self.__tela_inventario.mostra_mensagem(
                f"O item {arremesavel.nome} foi adicionado ao inventário!")
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Insira um arremesavel válido!")

    def adicionar_equipavel(self, equipavel):
        if isinstance(equipavel, Equipavel):
            self.__entidade_inventario.espaco_interno(equipavel)
            self.__tela_inventario.mostra_mensagem(
                f"O item {equipavel.nome} foi adicionado ao inventário!")
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Insira um equipamento válido!")

    def remover_item(self, nome_item):
        if isinstance(nome_item, str):
            opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
            if opcao_tipo_item == 1:
                if self.__entidade_inventario.espaco_interno[Arremesavel]:
                    for arremesavel in self.__entidade_inventario.espaco_interno[Arremesavel]:
                        if arremesavel.nome == nome_item:
                            self.__entidade_inventario.espaco_interno[Arremesavel].remove(
                                arremesavel)
                            self.__tela_inventario.mostra_mensagem(
                                f"O item {arremesavel} foi deletado com sucesso!")
                            break
                    self.__tela_inventario.mostra_mensagem(
                        "Você não possui esse item")
                else:
                    self.__tela_inventario.mostra_mensagem(
                        "A lista de itens está vazia")
            elif opcao_tipo_item == 2:
                if self.__entidade_inventario.espaco_interno[Equipavel]:
                    for equipavel in self.__entidade_inventario.espaco_interno[Equipavel]:
                        if equipavel.nome == nome_item:
                            self.__entidade_inventario.espaco_interno[Equipavel].remove(
                                equipavel)
                            self.__tela_inventario.mostra_mensagem(
                                f"O item {equipavel} foi deletado com sucesso!")
                            break
                    self.__tela_inventario.mostra_mensagem(
                        "Você não possui esse item")
                else:
                    self.__tela_inventario.mostra_mensagem(
                        "A lista de itens está vazia")
            elif opcao_tipo_item == 3:
                if self.__entidade_inventario.espaco_interno[Consumivel]:
                    for consumivel in self.__entidade_inventario.espaco_interno[Consumivel]:
                        if consumivel.nome == nome_item:
                            self.__entidade_inventario.espaco_interno[Consumivel].remove(
                                consumivel)
                            self.__tela_inventario.mostra_mensagem(
                                f"O item {consumivel} foi deletado com sucesso!")
                            break
                    self.__tela_inventario.mostra_mensagem(
                        "Você não possui esse item")
                else:
                    self.__tela_inventario.mostra_mensagem(
                        "A lista de itens está vazia")
            elif opcao_tipo_item == 0:
                self.mostra_tela()
            else:
                self.__tela_inventario.mostra_mensagem(
                    "ERRO: Tipo de item inválido!")

    def listar_itens(self, tipo_item):
        for item in self.__entidade_inventario.espaco_interno[tipo_item]:
            self.__tela_inventario.mostra_mensagem(f"{item.nome}")

    def listar_inventario(self):
        tipos_item = {1: Consumivel, 2: Arremesavel, 3: Equipavel}
        contador = 1
        while contador <= 3:
            for item in self.__entidade_inventario.espaco_interno[contador]:
                self.__tela_inventario.mostra_mensagem(f"{item.nome}")
            contador += 1

    def atualizar_consumivel(self, item_ser_atualizado, mudar_atributo, novo_valor):
        if mudar_atributo not in (1, 2, 3, 4, 6):
            self.__tela_inventario.mostra_mensagem("ERRO: O item não possui esse atributo!")
            self.mostra_tela()
        for item in self.__entidade_inventario.espaco_interno[Consumivel]:
            if item.nome == item_ser_atualizado:
                if mudar_atributo == 1:
                    item.nome = novo_valor
                elif mudar_atributo == 2:
                    item.valor = novo_valor
                elif mudar_atributo == 3:
                    item.efeito = novo_valor
                elif mudar_atributo == 4:
                    item.dano = novo_valor
                else:
                    item.duracao = novo_valor


