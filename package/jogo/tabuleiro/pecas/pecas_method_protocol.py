from abc import ABC, abstractmethod
from casa import Casa

class Pecas_protocol(ABC):
    
    def movimento(pos_inicial: Casa) -> List : ...
    def is_valido(list: Casa) -> bool : ...