

class TelaJogador:
    def tela_opcoes(self):
        print("-------- Jogadores --------")
        print("Escolha uma opção")
        print("1 - Adicionar Jogador")
        print("2 - Editar Jogador")
        print("3 - Listar Jogadores")
        print("4 - Excluir Jogador")
        print("0 - Retornar")

        opcao = input("Escolha uma opção: ")
        opcoes_validas = ["1", "2", "3", "4", "0"]
        if opcao not in opcoes_validas:
            print("entrada inválida, tente novamente")
        else:
            return opcao

    def pega_dados_jogador(self):
        print("----- Dados do Jogador -----")
        nome = input("Nome: ")
        idade = input("Idade: ")

        return {"nome": nome, "idade": idade}

    def mostra_jogadores(self, dados_jogador):
        print("Nome :", dados_jogador["nome"])
        print("Idade :", dados_jogador["idade"])
        print("\n")

    def seleciona_jogador(self):
        nome = input("Nome do jogador que deseja selecionar: ")
        return nome

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
