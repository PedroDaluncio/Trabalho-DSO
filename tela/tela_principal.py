

class TelaPrincipal:
    def tela_opcoes(self):
        print("------CadastroRPG------")
        print("Escolha uma opção")
        print("1 - Jogadores")
        print("2 - Personagens")
        print("3 - Sessões")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        opcoes_validas = ["1", "2", "3", "0"]

        while opcao not in opcoes_validas:
            opcao = input("Entrada inválida, tente novamente: ")
        return int(opcao)
