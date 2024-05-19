import datetime


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

    def obter_data_sessao(self):
        print("insira a data da sessão ")
        ano = input("insira o ano: ")
        dia = input("insira o dia: ")
        mes = input("insira o mes: ")
        hora = input("insira apenas a hora: ")
        return {"ano": ano, "dia": dia, "mes": mes, "hora":hora}

    def mostrar_sessao(self, dados_sessao):
        print("Data da sessão: ", dados_sessao["data"])
        print("Jogadores participantes", dados_sessao["jogadores"])
        print("Personagens participantes", dados_sessao["personagens"])
        print("\n")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)