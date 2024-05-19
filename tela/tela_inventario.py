

class TelaInventario():

    #método que mostra as opções para o usuário
    def tela_opcoes(self):
        print("-------- INVENTÁRIO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Item")
        print("2 - Remover Item")
        print("3 - Listar Itens")
        print("4 - Listar Inventário")
        print("5 - Alterar Itens")
        print("0 - Retornar")
        opcao = int(input("Escolha a opção: "))
        #faz a verificação se a opção escolhida é valida
        while opcao < 0 or opcao > 5:
            opcao = input("Entrada inválida, digite novamente: ")
        return opcao

    #método que faz o usuário escolher um tipo de item
    def escolhe_tipo_item(self):
        self.mostra_mensagem('')
        print("-------- SELEÇÃO DO TIPO DE ITEM ----------")
        print("Escolha a opcao")
        print("1 - Arremesável")
        print("2 - Equipável")
        print("3 - Consumível")
        print("0 - Retornar")
        opcao = int(input("Escolha a opção: "))
        #verifica se a opção é valida
        while opcao not in (0, 1, 2, 3):
            opcao = input("Entrada inválida, digite novamente: ")
        self.mostra_mensagem('')
        return opcao

    #método que pega os dados de itens do tipo consumível
    def dados_consumivel(self):
        print("-------- DADOS CONSUMÍVEL ----------")
        nome = input("Nome: ")
        # verifica se a variavel nome possui apenas letras ou espaços
        # isalpha = é letra, isspace = é espaço, isdigit = é número
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in nome):
            nome = input("Nome inválido, insira novamente: ")
        valor = input("Valor: ")
        while not all(caractere.isdigit() for caractere in valor):
            valor = input("Valor inválido, insira novamente: ")
        efeito = input("Efeito: ")
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in efeito):
            efeito = input("Efeito inválido, insira novamente:")
        dano = input("Dano: ")
        while not all(caractere.isdigit() for caractere in dano):
            dano = input("Dano inválido, insira novamente: ")
        duracao = input("Duracao: ")
        while not all(caractere.isdigit() for caractere in duracao):
            duracao = input("Duracao inválido, insira novamente: ")
        return {"nome": nome, "valor": int(valor), "efeito": efeito,
                "dano": int(dano), "duracao": int(duracao)}

    #método que pega os dados do item do tipo Equipavel
    def dados_equipavel(self):
        print("-------- DADOS EQUIPAVEL ----------")
        nome = input("Nome: ")
        # verifica se a variavel nome possui apenas letras ou espaços
        # isalpha = é letra, isspace = é espaço, isdigit = é número
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in nome):
            nome = input("Nome inválido, insira novamente: ")
        valor = input("Valor: ")
        while not all(caractere.isdigit() for caractere in valor):
            valor = input("Valor inválido, insira novamente: ")
        efeito = input("Efeito: ")
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in efeito):
            efeito = input("Efeito inválido, insira novamente:")
        dano = input("Dano: ")
        while not all(caractere.isdigit() for caractere in dano):
            dano = input("Dano inválido, insira novamente: ")
        durabilidade = input("Durabilidade: ")
        while not all(caractere.isdigit() for caractere in durabilidade):
            durabilidade = input(
                "Durabilidade inválida, insira novamente: ")
        return {"nome": nome, "valor": int(valor), "efeito": efeito,
                "dano": int(dano), "durabilidade": int(durabilidade)}

    #método que pega os dados de item do tipo Arremesavel
    def dados_arremesavel(self):
        print("-------- DADOS ARREMESAVEL ----------")
        nome = input("Nome: ")
        # verifica se a variavel nome possui apenas letras ou espaços
        # isalpha = é letra, isspace = é espaço, isdigit = é número
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in nome):
            nome = input("Nome inválido, insira novamente: ")
        valor = input("Valor: ")
        while not all(caractere.isdigit() for caractere in valor):
            valor = input("Valor inválido, insira novamente: ")
        efeito = input("Efeito: ")
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in efeito):
            efeito = input("Efeito inválido, insira novamente:")
        dano = input("Dano: ")
        while not all(caractere.isdigit() for caractere in dano):
            dano = input("Dano inválido, insira novamente: ")
        alcance = input("Alcance: ")
        while not all(caractere.isdigit() for caractere in alcance):
            alcance = input("Alcance inválido, insira novamente: ")
        return {"nome": nome, "valor": int(valor), "efeito": efeito,
                "dano": int(dano), "alcance": int(alcance)}

    #método que pega o nome de um item que será removido
    def remover_item(self):
        nome_item = input(
            "Digite o nome do item que será removido: ")
        return nome_item

    #método que recebe uma lista de itens e mostra ela
    def listar_itens(self, lista_itens):
        for item in lista_itens:
            #faz a verificação se é o ultimo item na lista a fim de
            # arrumar a vírgula e espaço após o item
            if item == lista_itens[-1]:
                    print(item.nome, end="")
            else:
                print(item.nome, end=", ")
        print('')

    #método que lista todos os itens do Inventário
    #OBS: Ele é chamado três vezes, uma vez para cada tipo de item
    def listar_inventario(self, itens, tipo_item):
        print(f"Items do tipo {tipo_item}:")
        if not itens:
            print("Você não possui nenhum item desse tipo!")
        else:
            for item in itens:
                if item == itens[-1]:
                    print(item.nome, end="")
                else:
                    print(item.nome, end=", ")
            print('')

    #método que faz o usuário escolher um tipo de item
    def opcoes_atualizacao(self):
        print("-------- ATUALIZAR ITEM ----------")
        print("Escolha o que deseja atualizar")
        print("1 - Nome")
        print("2 - Valor")
        print("3 - Efeito")
        print("4 - Dano")
        print("5 - Alcance")
        print("6 - Duracao")
        print("7 - Durabilidade")
        print("0 - Voltar")
        opcao = int(input("Digite a sua escolha: "))
        #verifica se a opção digitada é valida
        while opcao < 0 or opcao > 7:
            opcao = int(input("ESCOLHA INVÁLIDA! INSIRA NOVAMENTE: "))
        return opcao

    #método que faz o usuário digitar o novo valor de um atributo do item
    def pega_dado_atualizacao(self):
        dado = input("Insira o novo valor: ")
        return dado

    #método que pega o nome do item que será atualizado
    def pega_nome_item_atualizar(self):
        nome_item = input("Digite o nome do item que será atualizado: ")
        return nome_item

    #método que mostra uma mensagem ao usuário
    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
