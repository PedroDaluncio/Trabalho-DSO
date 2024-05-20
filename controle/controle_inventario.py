from tela.tela_inventario import TelaInventario
from entidade.Inventario import Inventario
from outras_classes.Arremesavel import Arremesavel
from outras_classes.Consumivel import Consumivel
from outras_classes.Equipavel import Equipavel


class ControleInventario:
    def __init__(self, controle_personagem):
        self.__tela_inventario = TelaInventario()
        self.__entidade_inventario = Inventario()
        self.__controle_personagem = controle_personagem

    #método que irá criar o inventário para um personagem
    def cria_inventario(self, nome_personagem):
        self.__entidade_inventario.cria_inventario(nome_personagem, {
            Arremesavel: [],
            Consumivel: [],
            Equipavel: [],
        })

    #método que adicionara itens em um inventário
    def adicionar_item(self):
        #faz o usuário escolher um tipo de item para adicionar, ou seja
        #faz ele escolher entre Arremesavel, Consumivel e Equipavel
        tipo_item = self.__tela_inventario.escolhe_tipo_item()
        #verifica se será adicionado um arremesavel
        if tipo_item == 1:
            #pega os dados do item
            atributos_item = self.__tela_inventario.dados_arremesavel()
            #chama o setter do espaco_interno e passa a classe Arremesavel
            # e uma instância dela como parâmetros
            self.__entidade_inventario.espaco_interno = \
                Arremesavel, Arremesavel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["alcance"]
            )
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['nome']}"
                " foi adicionado ao inventário!")
            #adiciona o item na lista de itens adquiridos
            self.__entidade_inventario.itens_adquiridos = \
                atributos_item['nome']
        #verifica se será adicionado um equipavel
        elif tipo_item == 2:
            #pega os dados do item
            atributos_item = self.__tela_inventario.dados_equipavel()
            #chama o setter do espaco_interno e passa a classe Equipavel
            # e uma instância dela como parâmetros
            self.__entidade_inventario.espaco_interno = \
                Equipavel, Equipavel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["durabilidade"]
            )
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['nome']}"
                " foi adicionado ao inventário!")
            #adiciona o item na lista de itens adquiridos
            self.__entidade_inventario.itens_adquiridos = \
                atributos_item['nome']
        elif tipo_item == 3:
            atributos_item = self.__tela_inventario.dados_consumivel()
            #chama o setter do espaco_interno e passa a classe Consumivel
            # e uma instância dela como parâmetros
            self.__entidade_inventario.espaco_interno = \
                Consumivel, Consumivel(
                atributos_item["nome"],
                atributos_item["valor"],
                atributos_item["efeito"],
                atributos_item["dano"],
                atributos_item["duracao"]
            )
            self.__tela_inventario.mostra_mensagem(
                f"O item {atributos_item['nome']}"
                " foi adicionado ao inventário!")
            #adiciona o item na lista de itens adquiridos
            self.__entidade_inventario.itens_adquiridos = \
                atributos_item['nome']
        #verifica se o usuário quer voltar para a tela do inventário
        elif tipo_item == 0:
            self.mostra_tela()
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Insira um item válido!")
        self.__tela_inventario.mostra_mensagem('')

    #método que irá remover um item
    def remover_item(self):
        #faz o usuário escolher um tipo de item
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        #variável que é o espaço interno, foi feita dessa maneira para
        #economizar linhas
        inventario = self.__entidade_inventario.espaco_interno
        #verifica se o usuário escolheu um item do tipo Arremesavel
        if opcao_tipo_item == 1:
            #verifica se a lista de item está vazia
            if inventario[Arremesavel]:
                #lista todos os itens do tipo Arremesavel
                self.__tela_inventario.listar_itens(
                    inventario[Arremesavel])
                #recebe o nome do item que o usuário quer remover
                nome_item = self.__tela_inventario.remover_item()
                #verifica se o item existe
                for arremesavel in inventario[Arremesavel]:
                    if arremesavel.nome == nome_item:
                        #remove o item da lista
                        inventario[Arremesavel].remove(
                            arremesavel)
                        self.__tela_inventario.mostra_mensagem(
                            f"O item {arremesavel.nome}"
                            " foi deletado com sucesso!")
                        self.__entidade_inventario.itens_perdidos = \
                            arremesavel.nome
                        self.mostra_tela()
                self.__tela_inventario.mostra_mensagem(
                    "Você não possui esse item")
            else:
                self.__tela_inventario.mostra_mensagem(
                    "A lista de itens está vazia")
        #verifica se o usuário escolheu um item do tipo Equipavel
        elif opcao_tipo_item == 2:
            #verifica se a lista de itens está vazia
            if inventario[Equipavel]:
                #lista todos os itens do tipo Equipavel
                self.__tela_inventario.listar_itens(
                    inventario[Equipavel])
                #recebe qual item será removido
                nome_item = self.__tela_inventario.remover_item()
                #verifica se o item existe
                for equipavel in inventario[Equipavel]:
                    if equipavel.nome == nome_item:
                        inventario[Equipavel].remove(
                            equipavel)
                        self.__tela_inventario.mostra_mensagem(
                            f"O item {equipavel.nome}"
                            " foi deletado com sucesso!")
                        #adiciona o item na lista de itens perdidos
                        self.__entidade_inventario.itens_perdidos = \
                            equipavel.nome
                        self.mostra_tela()
                self.__tela_inventario.mostra_mensagem(
                    "Você não possui esse item")
            else:
                self.__tela_inventario.mostra_mensagem(
                    "A lista de itens está vazia")
        #verifica se o usuário escolheu um item do tipo Consumivel
        elif opcao_tipo_item == 3:
            #verifica se a lista de itens está vazia
            if inventario[Consumivel]:
                #lista todos os itens do tipo Consumivel
                self.__tela_inventario.listar_itens(inventario[
                    Consumivel])
                #recebe qual item será removido
                nome_item = self.__tela_inventario.remover_item()
                #verifica se o item existe
                for consumivel in inventario[Consumivel]:
                    if consumivel.nome == nome_item:
                        inventario[Consumivel].remove(
                            consumivel)
                        self.__tela_inventario.mostra_mensagem(
                            f"O item {consumivel.nome}"
                            " foi deletado com sucesso!")
                        #adiciona o item na lista de itens perdidos
                        self.__entidade_inventario.itens_perdidos = \
                            consumivel.nome
                        self.mostra_tela()
                self.__tela_inventario.mostra_mensagem(
                    "Você não possui esse item")
            else:
                self.__tela_inventario.mostra_mensagem(
                    "A lista de itens está vazia")
        #volta para a tela do inventário
        elif opcao_tipo_item == 0:
            self.__tela_inventario.mostra_mensagem('')
            self.mostra_tela()
        else:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: Tipo de item inválido!")
        self.__tela_inventario.mostra_mensagem('')

    #lista todos os itens de um determinado tipo
    def listar_itens(self):
        #escolhe que tipo de item será listado
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        #dicionário contendo os tipos de itens
        tipo_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
        #verifica se o usuário digitou 0, ou seja, se ele quer
        # voltar para a tela de itens
        if not opcao_tipo_item:
            self.mostra_tela()
        #verifica se a lista de itens está vazia
        elif not self.__entidade_inventario.espaco_interno[
            tipo_item[opcao_tipo_item]]:
            self.__tela_inventario.mostra_mensagem(
                "ERRO: A LISTA DE ITENS ESTÁ VAZIA!")
            self.mostra_tela()
        #seleciona a lista de itens que será mostrada
        itens = self.__entidade_inventario.espaco_interno[
            tipo_item[opcao_tipo_item]]
        #lista os itens contidos dentro de itens
        self.__tela_inventario.listar_itens(itens)

    #lista todos os itens do personagem
    def listar_inventario(self):
        #dicionário contendo os tipos de item
        tipos_item = {1: Arremesavel, 2: Consumivel, 3: Equipavel}
        #seleciona o inventário. Foi feito dessa maneira para economizar
        #espaço
        itens = self.__entidade_inventario.espaco_interno
        #Dicionário contendo os tipos de item versão string
        str_tipos_item = {1: "Arremesavel",
                          2: "Consumivel",
                          3: "Equipavel"}
        #verifica se todas as listas estão vazias
        if not itens[Arremesavel] and \
            itens[Consumivel] and itens[Equipavel]:
                self.__tela_inventario.mostra_mensagem(
                    "ERRO: A LISTA DE ITENS ESTÁ VAZIA!")
                self.mostra_tela()
        contador = 1
        while contador <= 3:
            #chama o método na tela para listar os itens
            self.__tela_inventario.listar_inventario(
                itens[tipos_item[contador]], str_tipos_item[contador])
            contador += 1
        self.__tela_inventario.mostra_mensagem('')

    #método que irá atualizar um item
    def atualizar_item(self):
        #faz o usuário escolher qual tipo de item será atualizado
        opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
        #verifica se ele quer voltar para a tela do inventário
        if opcao_tipo_item == 0:
            self.mostra_tela()
        #dicionário contendo os tipos de item
        tipo_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
        #seleciona os itens de um determinado tipo que estão cadastrados
        #no inventário
        inventario_tipo_item = self.__entidade_inventario.espaco_interno[
            tipo_item[opcao_tipo_item]]
        #verifica se o inventário está vazio
        if inventario_tipo_item:
            #escolhe o item que será atualizado
            item_ser_atualizado = \
                self.__tela_inventario.pega_nome_item_atualizar()
            for item in inventario_tipo_item:
                if item.nome == item_ser_atualizado:
                    #escolhe qual atributo será atualizado
                    mudar_atributo = \
                        self.__tela_inventario.opcoes_atualizacao()
                    #pega o novo valor do atributo escolhido
                    novo_valor = \
                        self.__tela_inventario.pega_dado_atualizacao()
                    #realiza a verificação de qual atributo será
                    # atualizado
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
                elif item == inventario_tipo_item[-1] and \
                    item.nome != item_ser_atualizado:
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

    #método que muda qual personagem está acessando o inventário
    def atualizar_personagem_inventario(self, personagem):
        self.__entidade_inventario.personagem = personagem

    #método que retorna os itens necessários para realizar o relatório
    def pega_itens_relatorio(self):
        return [self.__entidade_inventario.itens_adquiridos,
                self.__entidade_inventario.itens_perdidos]

    #método que mostra as opções do inventário para o usuário
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
