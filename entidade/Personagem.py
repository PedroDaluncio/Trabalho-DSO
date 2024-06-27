

class Personagem():
    def __init__(self, nome, nivel, classe, raca):
        #nome so personagem
        self.__nome = nome
        #nível do personagem
        self.__nivel = nivel
        #classe do personagem
        self.__classe = classe
        #raça do personagem
        self.__raca = raca
        #quantos níveis o personagem ganhou, sendo utilizado no relatório
        self.__qt_niveis_adquiridos = 0
        self.__inventario = {}
        self.__itens_adquiridos = []
        self.__itens_perdidos = []

    #getters e setters:
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, classe):
        self.__classe = classe

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def qt_niveis_adquiridos(self):
        return self.__qt_niveis_adquiridos

    @qt_niveis_adquiridos.setter
    def qt_niveis_adquiridos(self, qt_niveis):
        self.__qt_niveis_adquiridos = qt_niveis

    @property
    def inventario(self):
        return self.__inventario

    @inventario.setter
    def inventario(self, parametros):
        classe, item = parametros
        self.__inventario[classe].append(item)

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

    def cria_inventario(self, inventario):
        self.__inventario = inventario
