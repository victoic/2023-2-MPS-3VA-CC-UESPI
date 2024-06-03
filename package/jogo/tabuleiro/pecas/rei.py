from typing import List
from pecas_method_protocol import Pecas_protocol
from casa import Casa

class Rei(Pecas_protocol):

    def __init__(self, roque_feito : bool):
        self.roque_feito = roque_feito
        
    def movimento(pos_inicial: Casa) -> List:
        return super().movimento()
    
    def is_valido(list: Casa) -> bool:
        return super().is_valido()