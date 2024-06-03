from pecas_method_protocol import Pecas_protocol
from casa import Casa
from typing import List

class Torre(Pecas_protocol):
    
    def __init__(self) -> None:
        self._first_play_torre = True
    
    def movimento(pos_inicial:Casa) -> List:
        
        self._fist_play_king = False
        x = pos_inicial.x()
        y = pos_inicial.y()

        movimentos_possiveis = []
        movimentos_possiveis = []

        for i in range(8):
            if i != x:
                movimentos_possiveis.append((i, y))

        
        for j in range(8):
            if j != y:
                movimentos_possiveis.append((x, j))
        return movimentos_possiveis

    def is_valido(seld, casas: Casa) -> bool:
        for i in range(len(casas)):
            for verifica in casas[i]:
                if not verifica.get_pecas() is None:
                    return False
        return True

    def first_play_torre(self):
        return self._first_play_torre
    
    