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
        tipos_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
        if isinstance(nome_item, str):
            while True:
                opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
                if opcao_tipo_item == 1:
                    if self.__entidade_inventario.espaco_interno[Arremesavel]:
                        for arremesavel in self.__entidade_inventario.espaco_interno[Arremesavel]:
                            if arremesavel.nome == nome_item:
                                self.__entidade_inventario.espaco_interno[Arremesavel].remove(arremesavel)
                                print(f"O item {arremesavel} foi deletado com sucesso!")
                                break
                        print("Você não possui esse item")
                    else:
                        print("A lista de itens está vazia")
                elif opcao_tipo_item == 2:
                    if self.__entidade_inventario.espaco_interno[Equipavel]:
                        for equipavel self.__entidade_inventario.espaco_interno[Equipavel]:
                            if equipavel.nome == nome_item:
                                self.__entidade_inventario.espaco_interno[Equipavel].remove(equipavel)
                                print(f"O item {equipavel} foi deletado com sucesso!")
                                break
                        print("Você não possui esse item")
                    else:
                        print("A lista de itens está vazia")







a = {Consumivel: [Consumivel(15, "a", 45, "a", 78)]}
a[Consumivel].append("ola")


