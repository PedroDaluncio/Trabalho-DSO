

class AtualizarItemException(Exception):
    def __init__(self):
        super().__init__('ERRO: O ITEM NÃO POSSUI ESSE ATRIBUTO!')

