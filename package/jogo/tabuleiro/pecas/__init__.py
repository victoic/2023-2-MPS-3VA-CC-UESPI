from casa import Casa
from abc import ABC, abstractmethod

class Peca:
    def __init__(self):
        pass

    def is_branca(self):
        if(self == "branca"):
            return True
        else:
            False

    def is_morta(self):
        pass

    @abstractmethod
    def movimento():
        pass

    @abstractmethod
    def is_valido():
        pass