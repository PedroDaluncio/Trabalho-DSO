

class TelaPersonagem:

    def tela_opcoes(self):
        print("-------- OPÇÕES PERSONAGEM ----------")
        print("Escolha a opção")
        print("1 - Incluir Personagem")
        print("2 - Remover Personagem")
        print("3 - Listar Personagens")
        print("4 - Atualizar Personagem")
        print("5 - Acessar Inventário")
        print("6 - Gerar Relatório")
        print("0 - Retornar")
        opcao = int(input("Escolha a opção: "))
        while opcao not in (0, 1, 2, 3, 4, 5, 6):
            opcao = input("Entrada inválida, digite novamente: ")
        return opcao

    def pega_dados_personagem(self):
        print("-------- DADOS PERSONAGEM ----------")
        nome = input("Nome: ")
        # verifica se a variavel nome possui apenas letras ou espaços
        # isalpha = é letra, isspace = é espaço, isdigit = é número
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in nome):
            nome = input("Nome inválido, insira novamente: ")
        nivel = input("Nivel: ")
        while not all(caractere.isdigit() for caractere in nivel):
            nivel = input("Nivel inválido, insira novamente: ")
        classe = input("Classe: ")
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in classe):
            classe = input("Classe inválida, insira novamente:")
        raca = input("Raça: ")
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in raca):
            raca = input("Raça inválida, insira novamente: ")
        return {"nome": nome, "nivel": int(nivel),
                "classe": classe, "raça": raca}

    def remover_personagem(self):
        nome_personagem = input(
            "Insira o nome do personagem que será removido: ")
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in nome_personagem):
            nome_personagem = input("Nome inválido, insira novamente")
        return nome_personagem

    def listar_personagens(self, lista_personagens):
        for personagem in lista_personagens:
            print(personagem.nome)

    def opcoes_atualizacao(self):
        print("-------- OPÇÕES ATUALIZAÇÃO DO PERSONAGEM ----------")
        print("Escolha a opção")
        print("1 - Mudar Nome")
        print("2 - Mudar Classe")
        print("3 - Mudar Nível")
        print("0 - Retornar")
        opcao = int(input("Escolha a opção: "))
        while opcao not in (0, 1, 2, 3):
            opcao = input("Entrada inválida, digite novamente: ")
        return opcao

    def pega_nome_personagem(self):
        personagem = input("Insira o nome do personagem: ")
        return personagem

    def pega_dado_atualizacao(self):
        dado = input("Insira o novo valor: ")
        return dado

    def mostra_mensagem(self, mensagem):
        print(mensagem)
