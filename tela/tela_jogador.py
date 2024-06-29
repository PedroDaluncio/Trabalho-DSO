import PySimpleGUI as sg


class TelaJogador:
    def tela_opcoes(self, dados):
        layout = [
            [sg.Text("---Jogadores---")],
            [sg.Table(values=dados, headings=["Nome", "Idade", "Personagens"], max_col_width=25,
                      enable_events=False,
                      auto_size_columns=True,
                      justification='c',
                      num_rows=10,
                      alternating_row_color='darkblue',
                      key='seleção',
                      tooltip='Lista com os Jogadores')],
            [sg.Button('Adicionar', key=1),
             sg.Button('Editar', key=2),
             sg.Button('Excluir', key=4)],
            [sg.Button('Atribuir Personagem', key=5),
             sg.Button('Retornar', key=0)]
        ]
        window = sg.Window('Tela Jogador', layout)
        button, values = window.read()
        window.close()
        try:
            return [button, values['seleção']]
        except KeyError:
            return [0, [0]]

    def pega_dados_jogador(self):

        print('----- Dados do Jogador -----')
        nome = input('Nome: ')
        while not all(caractere.isalpha() or caractere.isspace() for caractere in nome):
            nome = input('Nome inválido, tente novamente: ')
        idade = input('Idade: ')
        while not all(caractere.isdigit() or caractere.isspace() for caractere in idade):
            idade = input('Idade inválida, tente novamente: ')

        return {'nome': nome, 'idade': int(idade)}

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
