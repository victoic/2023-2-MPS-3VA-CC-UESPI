from abc import ABC, abstractmethod

class Pecas_protocol(ABC):
    
    def movimento(pos_inicial: Casa) -> List : ...
    def is_valido(list: Casa) -> bool : ...