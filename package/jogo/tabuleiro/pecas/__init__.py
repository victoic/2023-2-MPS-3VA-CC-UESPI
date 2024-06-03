
from abc import ABC, abstractmethod

class Peca:
    def __init__(self) -> None:
        pass

    def is_branca(self):
        pass

    def is_morta(self):
        pass

    @abstractmethod
    def movimento():
        pass

    @abstractmethod
    def is_valido():
        pass