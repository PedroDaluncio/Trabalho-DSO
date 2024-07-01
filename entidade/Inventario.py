

class Inventario:
    def __init__(self):
        #é o inventário de itens, onde cada personagem possui o seu
        #próprio inventário
        self.__espaco_interno = {}
        #dicionário que contém todos os itens obtidos por um determinado
        #personagem
        self.__itens_adquiridos = {}
        #dícionario que contém todos os itens perdidos de um determinado
        #personagem
        self.__itens_perdidos = {}

    @property
    def espaco_interno(self):
        return self.__espaco_interno

    @espaco_interno.setter
    def espaco_interno(self, parametros):
        classe, item = parametros
        self.__espaco_interno[classe].append(item)

    @property
    def itens_adquiridos(self):
        return self.__itens_adquiridos

    @itens_adquiridos.setter
    def itens_adquiridos(self, item):
        #adiciona o item na lista de itens adquiridos para o personagem
        #que está atualmente no inventário
        self.__itens_adquiridos.append(item)

    @property
    def itens_perdidos(self):
        return self.__itens_perdidos

    @itens_perdidos.setter
    def itens_perdidos(self, item):
        #adiciona o item na lista de itens perdidos para o personagem
        #que está atualmente no invetário
        self.__itens_perdidos.append(item)

    #cria o inventário para o personagem que está atualmente no
    #inventário, adicionando no espaço interno. Além disso, cria a lista
    #de itens adquiridos e itens perdidos para o personagem
    def cria_inventario(self, inventario):
        self.__espaco_interno = inventario
        self.__itens_adquiridos = []
        self.__itens_perdidos = []
