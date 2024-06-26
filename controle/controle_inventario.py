from tela.tela_inventario import TelaInventario
from entidade.Inventario import Inventario
from outras_classes.arremesavel import Arremesavel
from outras_classes.consumivel import Consumivel
from outras_classes.equipavel import Equipavel
from tratamento_excesoes.excecao_close import JanelaFechadaException
from tratamento_excesoes.excecao_atualizar_item import AtualizarItemException


class ControleInventario:
    def __init__(self, controle_personagem):
        self.__tela_inventario = TelaInventario()
        self.__entidade_inventario = Inventario()
        self.__controle_personagem = controle_personagem
        self.__personagem_no_inventario = ''

    #método que irá criar o inventário para um personagem
    def cria_inventario(self):
        self.__entidade_inventario.cria_inventario({
            Arremesavel: [],
            Consumivel: [],
            Equipavel: [],
        })
        return self.__entidade_inventario.espaco_interno

    #método que adicionara itens em um inventário
    def adicionar_item(self):
        try:
            #faz o usuário escolher um tipo de item para adicionar, ou seja
            #faz ele escolher entre Arremesavel, Consumivel e Equipavel
            tipo_item = self.__tela_inventario.escolhe_tipo_item()
            if tipo_item == 'ação interrompida':
                raise JanelaFechadaException()
            #verifica se será adicionado um arremesavel
            personagem = self.__controle_personagem.retorna_personagem(self.__personagem_no_inventario)
            if tipo_item == 1:
                #pega os dados do item
                atributos_item = self.__tela_inventario.dados_arremesavel()
                if atributos_item == 'ação interrompida':
                    raise JanelaFechadaException()
                #chama o setter do espaco_interno e passa a classe Arremesavel
                # e uma instância dela como parâmetros
                personagem.inventario = Arremesavel, Arremesavel(
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
                personagem.itens_adquiridos = \
                    atributos_item['nome']
            #verifica se será adicionado um equipavel
            elif tipo_item == 2:
                #pega os dados do item
                atributos_item = self.__tela_inventario.dados_equipavel()
                if atributos_item == 'ação interrompida':
                    raise JanelaFechadaException()
                #chama o setter do espaco_interno e passa a classe Equipavel
                # e uma instância dela como parâmetros
                personagem.inventario = \
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
                personagem.itens_adquiridos = \
                    atributos_item['nome']
            elif tipo_item == 3:
                atributos_item = self.__tela_inventario.dados_consumivel()
                if atributos_item == 'ação interrompida':
                    raise JanelaFechadaException()
                #chama o setter do espaco_interno e passa a classe Consumivel
                # e uma instância dela como parâmetros
                personagem.inventario = \
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
                personagem.itens_adquiridos = \
                    atributos_item['nome']
            self.__controle_personagem.atualiza_dao(personagem)
        except JanelaFechadaException:
            self.mostra_tela()

    #método que irá remover um item
    def remover_item(self):
        try:
            personagem = self.__controle_personagem.retorna_personagem(self.__personagem_no_inventario)
            #variável que é o espaço interno, foi feita dessa maneira para
            #economizar linhas
            inventario = personagem.inventario
            parametro_inventario = {'Arremesavel': [],
                                    'Consumivel': [],
                                    'Equipavel': []}
            contador = 1
            for key in list(inventario.keys()):
                for item in inventario[key]:
                    if contador == 1:
                        parametro_inventario['Arremesavel'].append(item.nome)
                    elif contador == 2:
                        parametro_inventario['Consumivel'].append(item.nome)
                    else:
                        parametro_inventario['Equipavel'].append(item.nome)
                contador += 1
            #verifica se o usuário escolheu um item do tipo Arremesavel
            item_excluir = self.__tela_inventario.pega_nome_item(parametro_inventario)
            if item_excluir == 'ação interrompida':
                raise JanelaFechadaException()
            if item_excluir[0] == 'Arremesavel':
                #verifica se a lista de item está vazia
                if inventario[Arremesavel]:
                    #verifica se o item existe
                    for arremesavel in inventario[Arremesavel]:
                        if arremesavel.nome == item_excluir[1]:
                            #remove o item da lista
                            inventario[Arremesavel].remove(
                                arremesavel)
                            self.__tela_inventario.mostra_mensagem(
                                f"O item {arremesavel.nome}"
                                " foi deletado com sucesso!")
                            personagem.itens_perdidos = \
                                arremesavel.nome
                else:
                    self.__tela_inventario.mostra_mensagem(
                        "A lista de itens está vazia")
            #verifica se o usuário escolheu um item do tipo Equipavel
            elif item_excluir[0] == 'Equipavel':
                #verifica se a lista de itens está vazia
                if inventario[Equipavel]:
                    #verifica se o item existe
                    for equipavel in inventario[Equipavel]:
                        if equipavel.nome == item_excluir[1]:
                            inventario[Equipavel].remove(
                                equipavel)
                            self.__tela_inventario.mostra_mensagem(
                                f"O item {equipavel.nome}"
                                " foi deletado com sucesso!")
                            #adiciona o item na lista de itens perdidos
                            personagem.itens_perdidos = \
                                equipavel.nome
                else:
                    self.__tela_inventario.mostra_mensagem(
                        "A lista de itens está vazia")
            #verifica se o usuário escolheu um item do tipo Consumivel
            elif item_excluir[0] == 'Consumivel':
                #verifica se a lista de itens está vazia
                if inventario[Consumivel]:
                    #verifica se o item existe
                    for consumivel in inventario[Consumivel]:
                        if consumivel.nome == item_excluir[1]:
                            inventario[Consumivel].remove(
                                consumivel)
                            self.__tela_inventario.mostra_mensagem(
                                f"O item {consumivel.nome}"
                                " foi deletado com sucesso!")
                            #adiciona o item na lista de itens perdidos
                            personagem.itens_perdidos = \
                                consumivel.nome
                else:
                    self.__tela_inventario.mostra_mensagem(
                        "A lista de itens está vazia")
            self.__controle_personagem.atualiza_dao(personagem)
            self.mostra_tela()
        except JanelaFechadaException:
            self.mostra_tela()

    #método que irá atualizar um item
    def atualizar_item(self):
        try:
            personagem = self.__controle_personagem.retorna_personagem(self.__personagem_no_inventario)
            #faz o usuário escolher qual tipo de item será atualizado
            opcao_tipo_item = self.__tela_inventario.escolhe_tipo_item()
            if opcao_tipo_item == 'ação interrompida':
                raise JanelaFechadaException()
            #dicionário contendo os tipos de item
            tipo_item = {1: Arremesavel, 2: Equipavel, 3: Consumivel}
            #seleciona os itens de um determinado tipo que estão cadastrados
            #no inventário
            inventario_tipo_item = personagem.inventario[
                tipo_item[opcao_tipo_item]]
            #verifica se o inventário está vazio
            if inventario_tipo_item:
                parametro_inventario = {}
                nomes = [item.nome for item in inventario_tipo_item]
                if opcao_tipo_item == 1:
                    parametro_inventario = {'Arremesavel': nomes}
                elif opcao_tipo_item == 2:
                    parametro_inventario = {'Equipavel': nomes}
                else:
                    parametro_inventario = {'Consumivel': nomes}
                #escolhe o item que será atualizado
                item_ser_atualizado = \
                    self.__tela_inventario.pega_nome_item(parametro_inventario)[1]
                if item_ser_atualizado == 'ação interrompida':
                    raise JanelaFechadaException()
                for item in inventario_tipo_item:
                    if item.nome == item_ser_atualizado:
                        #escolhe qual atributo será atualizado
                        mudar_atributo = \
                            self.__tela_inventario.opcoes_atualizacao()
                        if mudar_atributo == 'ação interrompida':
                            raise JanelaFechadaException()
                        #pega o novo valor do atributo escolhido
                        novo_valor = \
                            self.__tela_inventario.pega_dado_atualizacao()
                        if novo_valor == 'ação interrompida':
                            raise JanelaFechadaException()
                        #realiza a verificação de qual atributo será
                        # atualizado
                        try:
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
                                raise AtualizarItemException()
                        except AtualizarItemException as error:
                            self.__tela_inventario.mostra_mensagem(error)
                            self.mostra_tela()
            else:
                self.__tela_inventario.mostra_mensagem(
                    "ERRO! A lista de itens está vazia!")
                self.mostra_tela()
            self.__tela_inventario.mostra_mensagem(
                "O item foi atualizado com sucesso!")
            self.__controle_personagem.atualiza_dao(personagem)
        except JanelaFechadaException:
            self.mostra_tela()

    #método que muda qual personagem está acessando o inventário
    def atualizar_personagem_inventario(self, personagem):
        self.__personagem_no_inventario = personagem

    def criar_tabela(self):
        personagem = self.__controle_personagem.retorna_personagem(self.__personagem_no_inventario)
        linhas = []
        inventario = personagem.inventario
        keys_inventario = list(inventario.keys())
        max_len = max(len(inventario[keys_inventario[0]]), len(
            inventario[keys_inventario[1]]), len(inventario[keys_inventario[2]]))
        for i in range(max_len):
            arremesavel = inventario[keys_inventario[0]][i].nome if i < len(
                inventario[keys_inventario[0]]) else ''
            consumivel = inventario[keys_inventario[1]][i].nome if i < len(
                inventario[keys_inventario[1]]) else ''
            equipavel = inventario[keys_inventario[2]][i].nome if i < len(
                inventario[keys_inventario[2]]) else ''
            linhas.append([arremesavel, consumivel, equipavel])
        return linhas

    #método que mostra as opções do inventário para o usuário
    def mostra_tela(self):
        try:
            opcoes = {1: self.adicionar_item,
                      2: self.remover_item,
                      3: self.atualizar_item,
                      0: self.__controle_personagem.mostra_tela
                     }
            while True:
                opcao_escolhida = self.__tela_inventario.tela_principal(self.criar_tabela())
                if opcao_escolhida == 'ação interrompida':
                    raise JanelaFechadaException()
                opcoes[opcao_escolhida]()
        except JanelaFechadaException:
            self.__controle_personagem.mostra_tela()
