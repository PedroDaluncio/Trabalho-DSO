import PySimpleGUI as sg


class TelaSessao:
    def tela_opcoes(self, dados):
        layout = [
            [sg.Text("---Sessao---")],
            [sg.Table(values=[dados], headings=["Data", "Jogadores", "Personagens"], max_col_width=25,
                      enable_events=False,
                      auto_size_columns=True,
                      justification='c',
                      num_rows=10,
                      alternating_row_color='lightblue',
                      key='seleção',
                      tooltip='Lista com os Jogadores')],
            [sg.Button('Registrar', key=1),
             sg.Button('Editar', key=2),
             sg.Button('Excluir', key=4),
             sg.Button('Retornar', key=0)]
        ]
        window = sg.Window('Tela Sessão', layout)
        button, values = window.read()
        window.close()
        try:
            return [button, values['seleção']]
        except KeyError:
            return [0, [0]]

    def selecionar_edicao(self):
        print("Escolha o que deseja editar")
        print("1 - Editar Data")
        print("2 - Editar Jogadores")
        print("3 - Editar Personagens")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def selecionar_operacao(self):
        print("Escolha o que deseja fazer")
        print("1 - Adicionar")
        print("2 - Excluir")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def entrada_sim_ou_nao(self):
        escolha = input("digite 'sim' parece confirmar: ")
        return escolha

    def pega_nome_jogador(self):
        nome = input("Insira o nome do jogador: ")
        return nome

    def obter_data_sessao(self):
        layout = [
            [sg.Text(text="Insira a data da sessão")],
            [sg.Text(text="Insidra o dia", size=(20, 1)), sg.InputText(size=(15, 1), key="dia")],
            [sg.Text(text="Insidra o mês(em decimal)", size=(20, 1)), sg.InputText(size=(15, 1), key="mes")],
            [sg.Text(text="Insidra o ano", size=(20, 1)), sg.InputText(size=(15, 1), key="ano")],
            [sg.Text(text="Insidra apenas a hora", size=(20, 1)), sg.InputText(size=(15, 1), key="hora")],
            [sg.Ok(), sg.Cancel()]
        ]
        window = sg.Window("Inserir dados", layout)
        button, values = window.read()
        window.close()

        return button, values

    def mostrar_sessao(self, dados_sessao):
        print("Data da sessão: ", dados_sessao["data"])
        print("Jogadores participantes", dados_sessao["jogadores"])
        print("Personagens participantes", dados_sessao["personagens"].nome)
        print("\n")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
