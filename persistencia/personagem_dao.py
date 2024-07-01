from persistencia.dao import DAO
from entidade.Personagem import Personagem


class PersonagemDAO(DAO):
    def __init__(self):
        super().__init__("Personagem.pkl")

    def add(self, personagem: Personagem, **kwargs):
        if isinstance(personagem, Personagem):
            super().add(personagem.nome, personagem)

    def remove(self, personagem: Personagem):
        super().remove(personagem)
