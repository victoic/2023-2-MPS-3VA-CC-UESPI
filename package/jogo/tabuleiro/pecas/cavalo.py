from pecas_method_protocol import Pecas_protocol
from typing import List


class Cavalo(Pecas_protocol):

    def __init__(self) -> None:
        pass

    def movimento(pos_inicial: Casa) -> List:
        return super().movimento()
    
    def is_valido(list: Casa) -> bool:
        return super().is_valido()
        
    