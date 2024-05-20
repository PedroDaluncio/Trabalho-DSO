from tela.tela_inventario import TelaInventario
from entidade.Inventario import Inventario
from outras_classes.Arremesavel import Arremesavel
from outras_classes.Consumivel import Consumivel
from outras_classes.equipavel import Equipavel


class ControleInventario:
    def __init__(self, controle_personagem):
        self.__tela_inventario = TelaInventario()
        self.__entidade_inventario = Inventario()
        self.__controle_personagem = controle_personagem

    def cria_inventario(self, nome_personagem):
        self.__entidade_inventario.cria_inventario(nome_personagem , {
            Arremesavel: [],
            Consumivel: [],
            Equipavel: [],
        })
        self.__entidade_inventario.personagem = nome_personagem

    def adicionar_item(self):
        tipo_item = self.__tela_inventario.escolhe_tipo_item()
        if tipo_item == 1:
            atributos_item = self.__tela_inventario.dados_arremesavel()
            # chama o setter do espaco_interno e passa a classe Arremesavel e uma instância dela como parâmetros
            self.__entidade_inventario.espaco_interno = Arremesavel, Arremesavel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["alcance"]
            )
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['nome']} foi adicionado ao inventário!")
            self.__entidade_inventario.itens_adquiridos = atributos_item['nome']
        elif tipo_item == 2:
            atributos_item = self.__tela_inventario.dados_equipavel()
            self.__entidade_inventario.espaco_interno = Equipavel, Equipavel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["durabilidade"]
            )
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['nome']} foi adicionado ao inventário!")
            self.__entidade_inventario.itens_adquiridos = atributos_item['nome']
        elif tipo_item == 3:
            atributos_item = self.__tela_inventario.dados_consumivel()
            self.__entidade_inventario.espaco_interno = Consumivel, Consumivel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["duracao"]
            )
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['nome']} foi adicionado ao inventário!")
            self.__entidade_inventario.itens_adquiridos = atributos_item['nome']
        elif tipo_item == 0:
            self.mostra_tela()
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Insira um item válido!")
        self.__tela_inventario.mostra_mensagem('')

    def remover_item(self):
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        inventario = self.__entidade_inventario.espaco_interno
        if opcao_tipo_item == 1:
            if inventario[Arremesavel]:
                self.__tela_inventario.listar_itens(inventario[Arremesavel])
                nome_item = self.__tela_inventario.remover_item()
                for arremesavel in inventario[Arremesavel]:
                    if arremesavel.nome == nome_item:
                        inventario[Arremesavel].remove(
                            arremesavel)
                        self.__tela_inventario.mostra_mensagem(
                            f"O item {arremesavel.nome} foi deletado com sucesso!")
                        self.__entidade_inventario.itens_perdidos = arremesavel.nome
                        return
                self.__tela_inventario.mostra_mensagem(
                    "Você não possui esse item")
            else:
                self.__tela_inventario.mostra_mensagem(
                    "A lista de itens está vazia")
        elif opcao_tipo_item == 2:
            if inventario[Equipavel]:
                self.__tela_inventario.listar_itens(inventario[Equipavel])
                nome_item = self.__tela_inventario.remover_item()
                for equipavel in inventario[Equipavel]:
                    if equipavel.nome == nome_item:
                        inventario[Equipavel].remove(
                            equipavel)
                        self.__tela_inventario.mostra_mensagem(
                            f"O item {equipavel.nome} foi deletado com sucesso!")
                        self.__entidade_inventario.itens_perdidos = equipavel.nome
                        return
                self.__tela_inventario.mostra_mensagem(
                    "Você não possui esse item")
            else:
                self.__tela_inventario.mostra_mensagem(
                    "A lista de itens está vazia")
        elif opcao_tipo_item == 3:
            if inventario[Consumivel]:
                self.__tela_inventario.listar_itens(inventario[Consumivel])
                nome_item = self.__tela_inventario.remover_item()
                for consumivel in inventario[Consumivel]:
                    if consumivel.nome == nome_item:
                        inventario[Consumivel].remove(
                                consumivel)
                        self.__tela_inventario.mostra_mensagem(
                            f"O item {consumivel.nome} foi deletado com sucesso!")
                        self.__entidade_inventario.itens_perdidos = consumivel.nome
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
        self.__tela_inventario.mostra_mensagem('')

    def listar_itens(self):
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        tipo_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
        if not opcao_tipo_item:
            return
        elif not self.__entidade_inventario.espaco_interno[tipo_item[opcao_tipo_item]]:
            self.__tela_inventario.mostra_mensagem("ERRO: A LISTA DE ITENS ESTÁ VAZIA!")
            return
        itens = self.__entidade_inventario.espaco_interno[
            tipo_item[opcao_tipo_item]]
        self.__tela_inventario.listar_itens(itens)
        self.__tela_inventario.mostra_mensagem('')

    def listar_inventario(self):
        tipos_item = {1: Arremesavel, 2: Consumivel, 3: Equipavel}
        itens = self.__entidade_inventario.espaco_interno
        str_tipos_item = {1: "Arremesavel",
                          2: "Consumivel",
                          3: "Equipavel"}
        if not itens[Arremesavel] and \
            itens[Consumivel] and itens[Equipavel]:
                self.__tela_inventario.mostra_mensagem("ERRO: A LISTA DE ITENS ESTÁ VAZIA!")
                return
        contador = 1
        while contador <= 3:
            self.__tela_inventario.listar_inventario(
                itens[tipos_item[contador]], str_tipos_item[contador])
            contador += 1
        self.__tela_inventario.mostra_mensagem('')

    def atualizar_item(self):
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        if opcao_tipo_item == 0:
            self.mostra_tela()
        tipo_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
        inventario_tipo_item = self.__entidade_inventario.espaco_interno[
            tipo_item[opcao_tipo_item]]
        if inventario_tipo_item:
            item_ser_atualizado = self.__tela_inventario.pega_nome_item_atualizar()
            mudar_atributo = self.__tela_inventario.opcoes_atualizacao()
            novo_valor = self.__tela_inventario.pega_dado_atualizacao()
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
        self.__tela_inventario.mostra_mensagem('')

    def atualizar_personagem_inventario(self, personagem):
        self.__entidade_inventario.personagem = personagem

    def pega_itens_relatorio(self):
        return [self.__entidade_inventario.itens_adquiridos,
                self.__entidade_inventario.itens_perdidos]

    def mostra_tela(self):
        opcoes = {1: self.adicionar_item,
                  2: self.remover_item,
                  3: self.listar_itens,
                  4: self.listar_inventario,
                  5: self.atualizar_item,
                  0: self.__controle_personagem.mostra_tela
                  }
        while True:
            self.__tela_inventario.mostra_mensagem('')
            opcoes[self.__tela_inventario.tela_opcoes()]()
