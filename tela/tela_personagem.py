import PySimpleGUI as sg


class TelaPersonagem:

    # lista as ações que podem ser feitas pela usuário
    def tela_opcoes(self):
        layout = [[sg.Button('Incluir Personagem', key=1), sg.Button('Remover Personagem', key=2)],
                  [sg.Button('Listar Personagens', key=3),
                   sg.Button('Atualizar Personagem', key=4)],
                  [sg.Button('Acessar Inventário', key=5),
                   sg.Button('Gerar Relatório', key=6)],
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
            elif not all(caractere.isdigit() for caractere in nivel) or nivel == '':
                sg.popup_error('O Nível do Personagem deve ser um número!')
            # Verificar se a classe não está vazia
            elif not all(caractere.isalpha() or caractere.isspace()
                         for caractere in classe) or not classe:
                sg.popup_error('A Classe do Personagem não pode estar vazia ou conter números')
            # Verificar se a raça não está vazia
            elif not all(caractere.isalpha() or caractere.isspace()
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
        button, values = window.Read()
        window.close()
        return values['nome']

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
        return button

    # faz o usuário escolher um personagem
    def pega_nome_personagem(self, lista_personagens):
        layout = [[sg.Text('Personagens cadastrados:')],
                  [sg.Combo(lista_personagens, size=(15,2), key='nome', default_value=lista_personagens[0])],
                  [sg.OK()]]

        window = sg.Window('PERSONAGENS CADASTRADOS').Layout(layout)
        button, values = window.Read()
        window.close()
        return values['nome']

    # faz o usuário digitar um novo valor para atualizar o personagem
    def pega_dado_atualizacao(self, atributo_ha_ser_atualizado):
        if atributo_ha_ser_atualizado == "classe":
            layout = [[sg.Text('Insira a nova classe do personagem:', size=(30, 1)), sg.Input(key="classe")],
                      [sg.Submit(), sg.Cancel()]]
            window = sg.Window('DADOS DO PERSONAGEM').Layout(layout)
            while True:
                button, values = window.Read()

                if button in (sg.WIN_CLOSED, 'Cancel'):
                    break

                if not all(caractere.isalpha() or caractere.isspace()
                        for caractere in values["classe"]) or not values["classe"]:
                    sg.popup_error('A Classe do Personagem não pode estar vazia ou conter números')
                else:
                    window.close()
                    return values["classe"]
        else:
            layout = [[sg.Text('Insira o novo nível do personagem:', size=(30, 1)), sg.Input(key="nivel")],
                      [sg.Submit(), sg.Cancel()]]
            window = sg.Window('DADOS DO PERSONAGEM').Layout(layout)
            while True:
                button, values = window.Read()

                if button in (sg.WIN_CLOSED, 'Cancel'):
                    break

                if not all(caractere.isdigit() for caractere in values["nivel"]) or values["nivel"] == '':
                    sg.popup_error('O Nível do Personagem deve ser um número!')
                else:
                    window.close()
                    return int(values["nivel"])

    # mostra o relatório para o usuário
    def mostra_relatorio(self, relatorio):
        itens_adquiridos = ''
        itens_perdidos = ''
        # verifica se o usuário adquiriu algum item
        if relatorio['Itens Adquiridos']:
            itens_adquiridos = sg.Listbox(relatorio['Itens Adquiridos'], size=(5,7))
        else:
            itens_adquiridos = sg.Text("O PERSONAGEM NÃO ADQUIRIU NENHUM ITEM NOVO!")
        # verifica se o usuário perdeu algum item
        if relatorio['Itens Perdidos']:
            itens_perdidos = sg.Listbox(relatorio['Itens Perdidos'], size=(5,7))
        else:
            itens_perdidos = sg.Text("O PERSONAGEM NÃO PERDEU NENHUM ITEM!")

        layout = [[sg.Text(f"QUANTIDADE DE NÍVEIS UPADOS: {relatorio['Niveis']}")],
                  [itens_adquiridos],
                  [itens_perdidos],
                  [sg.Ok()]]
        window = sg.Window('RELATORIO').Layout(layout)
        button, values = window.Read()
        window.close()

    # mostra uma mensagem ao usuário
    def mostra_mensagem(self, mensagem):
        layout = [[sg.Text(mensagem)],
                  [sg.Ok(size=(5, 2))]]
        window = sg.Window('AVISO').Layout(layout)
        button, values = window.Read()
        window.close()
