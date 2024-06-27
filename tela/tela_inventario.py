import PySimpleGUI as sg


class TelaInventario:

    # método que mostra as opções para o usuário
    def tela_principal(self, inventario):
        layout = [
            [sg.Table(values=inventario, headings=['Arremesavel', 'Consumivel', 'Equipavel'], key='-TABLE-',
                      enable_events=False, display_row_numbers=False)],
            [sg.Button('Adicionar Item', key=1), sg.Button('Remover Item', key=2) ,sg.Button('Editar Item', key=3)]
                ]
        window = sg.Window('INVENTÁRIO').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)

    # método que faz o usuário escolher um tipo de item
    def escolhe_tipo_item(self):
        layout = [[sg.Text('Escolha o tipo de item')],
                  [sg.Button('Arremesável', key=1), sg.Button('Equipável', key=2)],
                  [sg.Button('Consumível', key=3), sg.Cancel()]]

        window = sg.Window('SELEÇÃO DE TIPO DE ITEM').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)

    # método que pega os dados de itens do tipo consumível
    def dados_consumivel(self):
        layout = [[sg.Text('Nome:', size=(10, 1)), sg.Input(key='nome')],
                  [sg.Text('Valor:', size=(10, 1)), sg.Input(key='valor')],
                  [sg.Text('Efeito:', size=(10, 1)), sg.Input(key='efeito')],
                  [sg.Text('Dano:', size=(10, 1)), sg.Input(key='dano')],
                  [sg.Text('Duracao:', size=(10,1)), sg.Input(key='duracao')],
                  [sg.Submit(), sg.Cancel()]]

        window = sg.Window('DADOS CONSUMIVEL').Layout(layout)
        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancel'):
                break

            nome = values['nome']
            valor = values['valor']
            efeito = values['efeito']
            dano = values['dano']
            duracao = values['duracao']

            # Verificar se o nome contém apenas letras
            if not all(caractere.isalpha() or caractere.isspace()
                       for caractere in nome) or not nome:
                sg.popup_error(
                    'O Nome do consumivel deve conter apenas letras.')
            # Verificar se o nível é um número
            elif not all(caractere.isdigit() for caractere in valor) or not valor:
                sg.popup_error('O valor do consumível deve ser um número!')
            # Verificar se a classe não está vazia
            elif not all(caractere.isalpha() or caractere.isspace()
                         for caractere in efeito) or not efeito:
                sg.popup_error('O efeito não pode estar vazio ou conter números')
            # Verificar se a raça não está vazia
            elif not all(caractere.isdigit() for caractere in dano) or not dano:
                sg.popup_error('O valor do dano deve ser um número')
            elif not all(caractere.isdigit() for caractere in duracao) or not duracao:
                sg.popup_error('O valor da duracao deve ser um número')
            else:
                window.close()
                return {"nome": nome, "valor": int(valor), "efeito": efeito,
                        "dano": int(dano), "duracao": int(duracao)}

    # método que pega os dados do item do tipo Equipavel
    def dados_equipavel(self):
        layout = [[sg.Text('Nome:', size=(10, 1)), sg.Input(key='nome')],
                  [sg.Text('Valor:', size=(10, 1)), sg.Input(key='valor')],
                  [sg.Text('Efeito:', size=(10, 1)), sg.Input(key='efeito')],
                  [sg.Text('Dano:', size=(10, 1)), sg.Input(key='dano')],
                  [sg.Text('Durabilidade:', size=(10,1)), sg.Input(key='durabilidade')],
                  [sg.Submit(), sg.Cancel()]]

        window = sg.Window('DADOS EQUIPAVEL').Layout(layout)
        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancel'):
                break

            nome = values['nome']
            valor = values['valor']
            efeito = values['efeito']
            dano = values['dano']
            durabilidade = values['durabilidade']

            # Verificar se o nome contém apenas letras
            if not all(caractere.isalpha() or caractere.isspace()
                       for caractere in nome) or not nome:
                sg.popup_error(
                    'O Nome do consumivel deve conter apenas letras.')
            # Verificar se o nível é um número
            elif not all(caractere.isdigit() for caractere in valor) or not valor:
                sg.popup_error('O valor do consumível deve ser um número!')
            # Verificar se a classe não está vazia
            elif not all(caractere.isalpha() or caractere.isspace()
                         for caractere in efeito) or not efeito:
                sg.popup_error('O efeito não pode estar vazio ou conter números')
            # Verificar se a raça não está vazia
            elif not all(caractere.isdigit() for caractere in dano) or not dano:
                sg.popup_error('O valor do dano deve ser um número')
            elif not all(caractere.isdigit() for caractere in durabilidade) or not durabilidade:
                sg.popup_error('O valor da durabilidade deve ser um número')
            else:
                window.close()
                return {"nome": nome, "valor": int(valor), "efeito": efeito,
                        "dano": int(dano), "durabilidade": int(durabilidade)}

    # método que pega os dados de item do tipo Arremesavel
    def dados_arremesavel(self):
        layout = [[sg.Text('Nome:', size=(10, 1)), sg.Input(key='nome')],
                  [sg.Text('Valor:', size=(10, 1)), sg.Input(key='valor')],
                  [sg.Text('Efeito:', size=(10, 1)), sg.Input(key='efeito')],
                  [sg.Text('Dano:', size=(10, 1)), sg.Input(key='dano')],
                  [sg.Text('Alcance:', size=(10,1)), sg.Input(key='alcance')],
                  [sg.Submit(), sg.Cancel()]]

        window = sg.Window('DADOS ARREMESAVEL').Layout(layout)
        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancel'):
                break

            nome = values['nome']
            valor = values['valor']
            efeito = values['efeito']
            dano = values['dano']
            alcance = values['alcance']

            # Verificar se o nome contém apenas letras
            if not all(caractere.isalpha() or caractere.isspace()
                       for caractere in nome) or not nome:
                sg.popup_error(
                    'O Nome do consumivel deve conter apenas letras.')
            # Verificar se o nível é um número
            elif not all(caractere.isdigit() for caractere in valor) or not valor:
                sg.popup_error('O valor do consumível deve ser um número!')
            # Verificar se a classe não está vazia
            elif not all(caractere.isalpha() or caractere.isspace()
                         for caractere in efeito) or not efeito:
                sg.popup_error('O efeito não pode estar vazio ou conter números')
            # Verificar se a raça não está vazia
            elif not all(caractere.isdigit() for caractere in dano) or not dano:
                sg.popup_error('O valor do dano deve ser um número')
            elif not all(caractere.isdigit() for caractere in alcance) or not alcance:
                sg.popup_error('O valor da durabilidade deve ser um número')
            else:
                window.close()
                return {"nome": nome, "valor": int(valor), "efeito": efeito,
                        "dano": int(dano), "alcance": int(alcance)}

    # método que faz o usuário escolher um tipo de item
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
        # verifica se a opção digitada é valida
        while opcao < 0 or opcao > 7:
            opcao = int(input("ESCOLHA INVÁLIDA! INSIRA NOVAMENTE: "))
        return opcao

    # método que faz o usuário digitar o novo valor de um atributo do item
    def pega_dado_atualizacao(self):
        dado = input("Insira o novo valor: ")
        return dado

    # método que pega o nome do item que será atualizado
    def pega_nome_item(self, inventario):
        layout = [[sg.Text('Escolha um tipo de item:'), sg.Combo(list(inventario.keys()), key='tipo_item', enable_events=True)],
                  [sg.Text('Itens:'), sg.Combo(values=[], key='itens', size=(20, 2))],
                  [sg.Submit(), sg.Cancel()]]

        values = ''
        window = sg.Window('ESCOLHA UM ITEM').Layout(layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Submit':
                break

            # Atualiza os valores da Listbox baseado na chave selecionada
            if event == 'tipo_item':
                selected_key = values['tipo_item']
                window['itens'].update(inventario[selected_key])

        window.close()
        print(values)
        return [values['tipo_item'], values['itens']]

    # método que mostra uma mensagem ao usuário
    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
