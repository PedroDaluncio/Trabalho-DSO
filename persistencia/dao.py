from abc import ABC, abstractmethod
import pickle


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, "rb"))

    def add(self, key, objeto):
        self.__cache[key] = objeto
        self.__dump()

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def save(self):
        self.__dump()

    def get_all(self):
        return list(self.__cache.values())
