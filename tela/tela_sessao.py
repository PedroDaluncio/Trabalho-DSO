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
        print("-------- Data da Sessão --------")
        data = input("insira a data da sessão no formato (dia, mês, ano, hora, minuto): ")
        if isinstance(data, datetime.datetime):
            return data
        else:
            self.mostrar_mensagem("data inválida")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)