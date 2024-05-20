

class TelaSessao:
    def tela_opcoes(self):
        print("-------- Sessões --------")
        print("Escolha uma opção")
        print("1 - Registrar Sessão")
        print("2 - Alterar Sessão")
        print("3 - Listar Sessões")
        print("4 - Excluir Sessão")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")
        while opcao not in ["1", "2", "3", "4", "0"]:
            opcao = input("OPÇÃO INVÁLIDA, TENTE NOVAMENTE: ")
        return int(opcao)

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
        print("insira a data da sessão ")
        dia = input("insira o dia: ")
        mes = input("insira o mês(em decimal): ")
        ano = input("insira o ano: ")
        hora = input("insira apenas a hora: ")
        return {"ano": int(ano), "dia": int(dia),
                "mes": int(mes), "hora": int(hora)}

    def mostrar_sessao(self, dados_sessao):
        print("Data da sessão: ", dados_sessao["data"])
        print("Jogadores participantes", dados_sessao["jogadores"])
        print("Personagens participantes", dados_sessao["personagens"].nome)
        print("\n")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
