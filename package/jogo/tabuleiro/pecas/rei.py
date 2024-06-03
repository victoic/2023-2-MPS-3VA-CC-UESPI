from typing import List
<<<<<<< HEAD
from casa import Casa
=======
from pecas_method_protocol import Pecas_protocol
import sys
import os
from casa import Casa
from torre import Torre
from __init__ import Peca
sys.path.append(os.path.abspath( '../casa'))
sys.path.append(os.path.abspath( '../torre'))
sys.path.append(os.path.abspath( '../__init__'))



class Rei(Pecas_protocol, Peca):

    def __init__(self, ):
        self._roque_feito = None
        self._first_play_king = True

        
    def is_branca(self, peca):
        return peca

    def is_morta(self):
        pass

    def movimento(self, pos_inicial: Casa) -> List:

        self._fist_play_king = False
        x = pos_inicial.x()
        y = pos_inicial.y()

        movimentos_possiveis = []
        direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1),(0, 1),(1, -1), (1, 0), (1, 1)]

        for dx, dy in direcoes:
            novo_x, novo_y = x + dx, y + dy
            if 0 <= novo_x < 8 and 0 <= novo_y < 8:  
                movimentos_possiveis.append((novo_x, novo_y))

        return movimentos_possiveis
        
    
    def is_valido(seld, casas: Casa) -> bool:
        for i in range(len(casas)):
            for verifica in cassa[i]:
                if not verifica.get_pecas() is None:
                    return false
        return true

    def verificaTorre_isValid(self, torre : Torre) -> bool:
        return torre.first_play_torre()

    def is_safe(self) -> bool:
        pass

    def is_roque_valid(self):
        return self._first_play_king and self.verificaTorre_isValid() and self.is_safe()