import PySimpleGUI as sg


class TelaPersonagem:

    # lista as ações que podem ser feitas pela usuário
    def tela_opcoes(self):
        layout = [[sg.Button('Incluir Personagem', key=1), sg.Button('Remover Personagem', key=2)],
                  [sg.Button('Listar Personagens', key=3),
                   sg.Button('Atualizar Personagem', key=4)],
                  [sg.Button('Acessar Inventário', key=5),
                   sg.Button('Gerar Relatório')],
                  [sg.Button('Retornar', key=0)]
                  ]
        window = sg.Window('OPÇÕES PERSONAGEM').Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    # pergunta ao usuário os dados necessários para criar o personagem
    def pega_dados_personagem(self):
        layout = [[sg.Text('Nome do Personagem:', size=(20, 1)), sg.Input(key='nome')],
                  [sg.Text('Nível do Personagem:', size=(20, 1)),
                   sg.Input(key='nivel')],
                  [sg.Text('Classe do Personagem:', size=(20, 1)),
                   sg.Input(key='classe')],
                  [sg.Text('Raça do Personagem:', size=(20, 1)),
                   sg.Input(key='raça')],
                  [sg.Submit(), sg.Cancel()]]
        window = sg.Window('DADOS DO PERSONAGEM').Layout(layout)
        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancel'):
                break

            nome = values['nome']
            nivel = values['nivel']
            classe = values['classe']
            raca = values['raça']

            # Verificar se o nome contém apenas letras
            if not all(caractere.isalpha() or caractere.isspace()
                       for caractere in nome) or not nome:
                sg.popup_error(
                    'O Nome do Personagem deve conter apenas letras.')
            # Verificar se o nível é um número
            if not all(caractere.isdigit() for caractere in nivel) or nivel == '':
                sg.popup_error('O Nível do Personagem deve ser um número ou estar vazio')
            # Verificar se a classe não está vazia
            if not all(caractere.isalpha() or caractere.isspace()
                         for caractere in classe) or not classe:
                sg.popup_error('A Classe do Personagem não pode estar vazia ou conter números')
            # Verificar se a raça não está vazia
            if not all(caractere.isalpha() or caractere.isspace()
                         for caractere in raca) or not raca:
                sg.popup_error('A Raça do Personagem não pode estar vazia ou conter números')
            else:
                window.close()
                values['nivel'] = int(nivel)
                return values

   # faz o usuário escolher um personagem para ser excluido
    def remover_personagem(self, lista_personagens):
        layout = [[sg.Text('Escolha o personagem que será removido:'),
                   sg.Combo(lista_personagens, default_value=lista_personagens[0] ,key= 'nome')],
                  [sg.Submit(), sg.Cancel()]]

        window = sg.Window('REMOVER PERSONAGEM').Layout(layout)

        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancel'):
                break

            nome = values['nome']

            # Verificar se o nome contém apenas letras
            if not all(caractere.isalpha() or caractere.isspace()
                       for caractere in nome) or not nome:
                sg.popup_error(
                    'O Nome do Personagem deve conter apenas letras.')
            else:
                window.close()
                return nome

    # mostra todos os personagens existentes
    def listar_personagens(self, lista_personagens):
        layout = [[sg.Text('Personagens cadastrados:')],
                  [sg.Listbox(lista_personagens, size=(15,2))],
                  [sg.OK()]]

        window = sg.Window('PERSONAGENS CADASTRADOS').Layout(layout)
        button, values = window.Read()
        window.close()

    # faz o usuário escolher um atributo do personagem para atualizar
    def opcoes_atualizacao(self):
        layout = [[sg.Text('Escolha o que você quer mudar no personagem')],
                  [sg.Button('Classe', key="classe"), sg.Button('Nível', key="nivel")],
                  [sg.Cancel()]]
        window = sg.Window('ATUALIZAR PERSONAGEM').Layout(layout)
        button, values = window.Read()
        window.close()
        return values

    # faz o usuário escolher um personagem
    def pega_nome_personagem(self, lista_personagens):
        layout = [[sg.Text('Personagens cadastrados:')],
                  [sg.Listbox(lista_personagens, size=(15,2))],
                  [sg.OK()]]

        window = sg.Window('PERSONAGENS CADASTRADOS').Layout(layout)
        button, values = window.Read()
        window.close()
        return values[0][0]

    # faz o usuário digitar um novo valor para atualizar o personagem
    def pega_dado_atualizacao(self):
        dado = input("Insira o novo valor: ")
        if not all(caractere.isalpha() or caractere.isspace()
                   for caractere in dado):
            while '.' or "-" in dado:
                dado = input("VALOR INVÁLIDO! INSIRA NOVAMENTE: ")
                if all(caractere.isdigit() for caractere in dado) and \
                        '.' not in dado:
                    dado = int(dado)
                    break
        return dado

    # mostra o relatório para o usuário
    def mostra_relatorio(self, relatorio):
        print("-------- RELATÓRIO ----------")
        print(f"QUANTIDADE DE NÍVEIS UPADOS: {relatorio['Niveis']}")
        # verifica se o usuário adquiriu algum item
        if relatorio['Itens Adquiridos']:
            for itens_ganhos in relatorio['Itens Adquiridos']:
                print('ITENS GANHOS:')
                print(itens_ganhos, end="")
                if relatorio['Itens Adquiridos'][-1]:
                    print('')
        else:
            print("O PERSONAGEM NÃO ADQUIRIU NENHUM ITEM NOVO!")
        # verifica se o usuário perdeu algum item
        if relatorio['Itens Perdidos']:
            for itens_perdidos in relatorio['Itens Perdidos']:
                print('ITENS PERDIDOS:')
                print(itens_perdidos, end="")
                # if relatorio['Itens Perdidos'][-1]:
                #     print('')
        else:
            print("O PERSONAGEM NÃO PERDEU NENHUM ITEM!")

    # mostra uma mensagem ao usuário
    def mostra_mensagem(self, mensagem):
        layout = [[sg.Text(mensagem)],
                  [sg.Ok(size=(5, 2))]]
        window = sg.Window('AVISO').Layout(layout)
        button, values = window.Read()
        window.close()
