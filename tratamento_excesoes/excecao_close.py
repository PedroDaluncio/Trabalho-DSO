

class JanelaFechadaException(Exception):
    def __init__(self):
        super().__init__('ERRO: A JANELA FOI FECHADA!')
