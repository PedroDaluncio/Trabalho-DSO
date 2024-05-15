

class TelaSessao:
    def tela_opcoes(self):
        print("-------- Sessões --------")
        print("Escolha uma opção")
        print("1 - Registrar Sessão")
        print("2 - Alterar Sessão")
        print("3 - Listar Sessões")
        print("4 - Excluir Sessão")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))
        return opcao
    def obter_dados_sessao(self):
        print("-------- Dados da Sessão --------")
        data = input("")