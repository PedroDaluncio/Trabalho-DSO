

class TelaPersonagem:

    #lista as ações que podem ser feitas pela usuário
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
        #força o usuário a digitar novamente uma opção caso ele insira
        #uma opção inválida
        while opcao not in (0, 1, 2, 3, 4, 5, 6):
            opcao = input("Entrada inválida, digite novamente: ")
        return opcao

    #pergunta ao usuário os dados necessários para criar o personagem
    def pega_dados_personagem(self):
        print("-------- DADOS PERSONAGEM ----------")
        nome = input("Nome: ")
        # verifica se a variavel nome possui apenas letras ou espaços
        # isalpha = é letra, isspace = é espaço, isdigit = é número
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in nome):
            nome = input("Nome inválido, insira novamente: ")
        nivel = input("Nivel: ")
        #verifica se o níveis possui apenas dígitos
        while not all(caractere.isdigit() for caractere in nivel):
            nivel = input("Nivel inválido, insira novamente: ")
        classe = input("Classe: ")
        #verifica se a classe possui apenas espaço ou caracteres
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in classe):
            classe = input("Classe inválida, insira novamente:")
        raca = input("Raça: ")
        #verifica se a raça possui apenas espaço ou caracteres
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in raca):
            raca = input("Raça inválida, insira novamente: ")
        return {"nome": nome, "nivel": int(nivel),
                "classe": classe, "raça": raca}

    #faz o usuário escolher um personagem para ser excluido
    def remover_personagem(self):
        nome_personagem = input(
            "Insira o nome do personagem que será removido: ")
        #verifica se o nome do personagem é apenas caracteres ou espaço
        while not all(caractere.isalpha() or caractere.isspace()
                      for caractere in nome_personagem):
            nome_personagem = input("Nome inválido, insira novamente")
        return nome_personagem

    #mostra todos os personagens existentes
    def listar_personagens(self, lista_personagens):
        print("PERSONAGENS ATUALMENTE CADASTRADOS:")
        for personagem in lista_personagens:
            #faz uma verificação para inserir ou não a vírgula após o
            # nome do personagem
            if personagem == lista_personagens[-1]:
                print(personagem.nome, end='')
            else:
                print(personagem.nome, end=', ')
        print('')

    #faz o usuário escolher um atributo do personagem para atualizar
    def opcoes_atualizacao(self):
        print("-------- OPÇÕES ATUALIZAÇÃO DO PERSONAGEM ----------")
        print("Escolha a opção")
        print("1 - Mudar Classe")
        print("2 - Mudar Nível")
        print("0 - Retornar")
        opcao = int(input("Escolha a opção: "))
        #verifica se a opção é válida
        while opcao not in (0, 1, 2):
            opcao = input("Entrada inválida, digite novamente: ")
        return opcao

    #faz o usuário escolher um personagem
    def pega_nome_personagem(self):
        personagem = input("Insira o nome do personagem: ")
        return personagem

    #faz o usuário digitar um novo valor para atualizar o personagem
    def pega_dado_atualizacao(self):
        dado = input("Insira o novo valor: ")
        if not all(caractere.isalpha() or caractere.isspace() \
            for caractere in dado):
            while '.' or "-" in dado:
                dado = input("VALOR INVÁLIDO! INSIRA NOVAMENTE: ")
                if all(caractere.isdigit() for caractere in dado) and \
                    '.' not in dado:
                        dado = int(dado)
                        break
        return dado

    #mostra o relatório para o usuário
    def mostra_relatorio(self, relatorio):
        print("-------- RELATÓRIO ----------")
        print(f"QUANTIDADE DE NÍVEIS UPADOS: {relatorio['Niveis']}")
        #verifica se o usuário adquiriu algum item
        if relatorio['Itens Adquiridos']:
            for itens_ganhos in relatorio['Itens Adquiridos']:
                print('ITENS GANHOS:')
                print(itens_ganhos, end="")
                # if relatorio['Itens Adquiridos'][-1]:
                #     print('')
        else:
            print("O PERSONAGEM NÃO ADQUIRIU NENHUM ITEM NOVO!")
        print('')
        #verifica se o usuário perdeu algum item
        if relatorio['Itens Perdidos']:
            for itens_perdidos in relatorio['Itens Perdidos']:
                print('ITENS PERDIDOS:')
                print(itens_perdidos, end="")
                # if relatorio['Itens Perdidos'][-1]:
                #     print('')
        else:
            print("O PERSONAGEM NÃO PERDEU NENHUM ITEM!")

    #mostra uma mensagem ao usuário
    def mostra_mensagem(self, mensagem):
        print(mensagem)
