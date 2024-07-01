import PySimpleGUI as sg


class TelaPrincipal:
    def tela_opcoes(self):
        layout = [
            [sg.Text("Bem vindo ao cadastro de RPG, por favor escolha uma opção", size=(30, 2))],
            [sg.Button("Jogadores", size=(20, 2), key=1)],
            [sg.Button("Personagens", size=(20, 2), key=2)],
            [sg.Button("Sessões", size=(20, 2), key=3)],
            [sg.Button("Sair", size=(20, 2), key=0)]
        ]

        window = sg.Window("Cadastro RPG", size=(300, 270), element_justification="c").Layout(layout)
        button, values = window.Read()
        window.close()
        return button
