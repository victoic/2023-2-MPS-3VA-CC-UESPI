from typing import List, Any
from transformavel import Transformavel
from pecas_method_protocol import Pecas_protocol


class Piao(Transformavel, Pecas_protocol):
    def __init__(self) -> None:
         pass
     
     
     #Any será substituido Casa
    def movimentos(self, pos_inicial : Any) -> List:
         pass
    
     #Any será substituido Casa
    def is_valido(list: Any) -> bool:
        pass
    
    def transformar(self) -> Peca:
        pass