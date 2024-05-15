

class TelaInventario():

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
        while opcao not in (0, 1, 2, 3, 4, 5):
            opcao = input("Entrada inválida, digite novamente: ")
        return opcao

    def escolhe_tipo_item(self):
        print("-------- SELEÇÃO DO TIPO DE ITEM ----------")
        print("Escolha a opcao")
        print("1 - Arremesável")
        print("2 - Equipável")
        print("3 - Consumível")
        print("0 - Retornar")
        opcao = int(input("Escolha a opção: "))
        while opcao not in (0, 1, 2, 3):
            opcao = input("Entrada inválida, digite novamente: ")
        return opcao

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

    def dados_equipavel(self):
        print("-------- DADOS EQUIPÁVEL ----------")
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

    def remover_item(self):
        nome_item = input(
            "Digite o nome do item que será removido: ")
        return nome_item

    def listar_itens(self, lista_itens):
        for item in lista_itens:
            print(item.nome)

    def listar_inventario(self, inventario):
        for tipo_item in inventario:
            print(f"Items do tipo {tipo_item}:")
            for item in inventario[tipo_item]:
                if item == inventario[tipo_item][-1]:
                    print(item.nome, end="")
                else:
                    print(item.nome, end=", ")
            print("")

    def opcoes_atualizacao_arremesavel(self):
        print("-------- ATUALIZAR ITEM ----------")
        print("Escolha o que deseja atualizar")
        print("1 - Nome")
        print("2 - Valor")
        print("3 - Efeito")
        print("4 - Dano")
        print("5 - Alcance")
        print("0 - Voltar")
        opcao = input("Digite a sua escolha: ")
        return opcao

    def opcoes_atualizacao_equipavel(self):
        print("-------- ATUALIZAR ITEM ----------")
        print("Escolha o que deseja atualizar")
        print("1 - Nome")
        print("2 - Valor")
        print("3 - Efeito")
        print("4 - Dano")
        print("5 - Durabilidade")
        print("0 - Voltar")
        opcao = input("Digite a sua escolha: ")
        return opcao

    def opcoes_atualizacao_consumivel(self):
        print("-------- ATUALIZAR ITEM ----------")
        print("Escolha o que deseja atualizar")
        print("1 - Nome")
        print("2 - Valor")
        print("3 - Efeito")
        print("4 - Dano")
        print("5 - Duracao")
        print("0 - Voltar")
        opcao = input("Digite a sua escolha: ")
        return opcao

    def pega_nome_item_atualizar(self):
        nome_item = input("Digite o nome do item que será atualizado: ")
        return nome_item

    def pega_dado_atualizacao(self):
        dado = input("Insira o novo valor: ")
        return dado

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
