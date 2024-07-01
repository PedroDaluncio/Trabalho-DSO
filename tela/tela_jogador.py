import PySimpleGUI as sg


class TelaJogador:
    def tela_opcoes(self, dados):
        layout = [
            [sg.Text("---Jogadores---")],
            [sg.Table(values=dados, headings=["Nome", "Idade"], max_col_width=25,
                      enable_events=False,
                      auto_size_columns=True,
                      justification='c',
                      num_rows=10,
                      alternating_row_color='darkblue',
                      key='seleção',
                      tooltip='Lista com os Jogadores')],
            [sg.Button('Adicionar', key=1), sg.Button('Editar', key=2)],
            [sg.Button('Atribuir Personagem', key=5)],
            [sg.Button('Excluir', key=4), sg.Button('Retornar', key=0)]
        ]
        window = sg.Window('Tela Jogador', layout)
        button, values = window.read()
        window.close()
        try:
            return button, values['seleção']
        except KeyError:
            return 0, [0]

    def pega_dados_jogador(self):
        layout = [
            [sg.Text("Insira um nome", size=(15, 1)), sg.InputText(size=(15, 1), key="nome")],
            [sg.Text("Insira uma idade", size=(15, 1)), sg.InputText(size=(15, 1), key="idade")],
            [sg.Ok()]
        ]
        window = sg.Window("Dados do Jogador", layout)
        button, values = window.read()
        window.close()
        if button == "Ok":
            return values

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def tela_com_dois_botoes(self, mensagem, botao1, botao2):
        layout = [
            [sg.Text(mensagem, size=(20, 1))],
            [sg.Button(botao1, size=(10, 1), key=1),
             sg.Button(botao2, size=(10, 1), key=2)]
        ]
        window = sg.Window("Escolha", layout)
        escolha, values = window.read()
        window.close()
        return escolha

    def tela_de_input(self, mensagem):
        layout = [
            [sg.Text(mensagem, size=(15, 1))],
            [sg.InputText(size=(15, 1))],
            [sg.Ok()]
        ]
        window = sg.Window("Editar", layout)
        button, key = window.read()
        window.close()
        return key[0]

    def tela_com_todos(self, dados):
        layout = [
            [sg.Text("Adicione jogadores participantes")],
            [sg.Table(values=dados, headings=["Nome", "Idade", "Personagens"], max_col_width=25,
                      enable_events=False,
                      auto_size_columns=True,
                      justification='c',
                      num_rows=10,
                      alternating_row_color='darkblue',
                      key='seleção',
                      tooltip='Lista com os Jogadores')],
            [sg.Button('Adicionar', key='Adicionar'),
             [sg.Button('Finalizar', key='Finalizar')]]
        ]
        window = sg.Window('Tela Jogador', layout)
        button, values = window.read()
        window.close()
        try:
            return button, values['seleção']
        except KeyError:
            return 0, [0]
