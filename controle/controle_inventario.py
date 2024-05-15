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

    def adicionar_item(self):
        tipo_item = self.__tela_inventario.escolhe_tipo_item()
        if tipo_item == 1:
            atributos_item = self.__tela_inventario.dados_arremesavel()
            self.__entidade_inventario.espaco_interno(Arremesavel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["alcance"]
            ))
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['nome']} foi adicionado ao inventário!")
        elif tipo_item == 2:
            atributos_item = self.__tela_inventario.dados_equipavel()
            self.__entidade_inventario.espaco_interno(Equipavel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["durabilidade"]
            ))
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['durabilidade']} foi adicionado ao inventário!")
        elif tipo_item == 3:
            atributos_item = self.__tela_inventario.dados_consumivel()
            self.__entidade_inventario.espaco_interno(Consumivel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["duracao"]
            ))
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['duracao']} foi adicionado ao inventário!")
        elif tipo_item == 0:
            self.mostra_tela()
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Insira um item válido!")

    def remover_item(self):
        nome_item = self.__tela_inventario.remover_item()
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
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Insira um nome válido!"
            )

    def listar_itens(self):
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        tipo_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
        itens = self.__entidade_inventario.espaco_interno[
            tipo_item[opcao_tipo_item]]
        self.__tela_inventario.listar_itens(itens)

    def listar_inventario(self):
        tipos_item = {1: Consumivel, 2: Arremesavel, 3: Equipavel}
        itens = self.__entidade_inventario.espaco_interno()
        str_tipos_item = {1: "Consumivel",
                          2: "Arremesavel",
                          3: "Equipavel"}
        contador = 1
        while contador <= 3:
            self.__tela_inventario.listar_inventario(
                itens[tipos_item[contador]], str_tipos_item[contador])
            contador += 1

    def atualizar_item(self):
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        if opcao_tipo_item == 0:
            self.mostra_tela()
        tipo_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
        inventario_tipo_item = self.__entidade_inventario.espaco_interno[
            tipo_item[opcao_tipo_item]]()
        item_ser_atualizado = self.__tela_inventario.pega_nome_item_atualizar()
        mudar_atributo = self.__tela_inventario.opcoes_atualizacao()
        novo_valor = self.__tela_inventario.pega_dado_atualizacao()
        if inventario_tipo_item:
            for item in inventario_tipo_item:
                if item.nome == item_ser_atualizado:
                    if mudar_atributo == 1:
                        item.nome = novo_valor
                    elif mudar_atributo == 2:
                        item.valor = novo_valor
                    elif mudar_atributo == 3:
                        item.efeito = novo_valor
                    elif mudar_atributo == 4:
                        item.dano = novo_valor
                    elif mudar_atributo == 5 and opcao_tipo_item == 1:
                        item.alcance = novo_valor
                    elif mudar_atributo == 6 and opcao_tipo_item == 3:
                        item.duracao = novo_valor
                    elif mudar_atributo == 7 and opcao_tipo_item == 2:
                        item.durabilidade = novo_valor
                    else:
                        self.__tela_inventario.mostra_mensagem(
                            "ERRO: O item não possui esse atributo!")
                        self.mostra_tela()
                elif item == inventario_tipo_item[-1] and item.nome != item_ser_atualizado:
                    self.__tela_inventario.mostra_mensagem(
                        "ERRO! Você não possui esse item!")
                    self.mostra_tela()
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO! A lista de itens está vazia!")
            self.mostra_tela()
        self.__tela_inventario.mostra_mensagem(
            "O item foi atualizado com sucesso!")

    def mostra_tela(self):
        opcoes = {1: self.adicionar_item,
                  2: self.remover_item,
                  3: self.listar_itens,
                  4: self.listar_inventario,
                  5: self.atualizar_item,
                  0: self.__controle_personagem.mostra_tela}
        while True:
            opcoes[self.__tela_inventario.tela_opcoes()]()
