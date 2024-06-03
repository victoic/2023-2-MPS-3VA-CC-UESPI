from typing import List
from pecas_method_protocol import Pecas_protocol
import sys
import os
from casa import Casa
from torre import Torre
sys.path.append(os.path.abspath( '../casa'))
sys.path.append(os.path.abspath( '../torre'))



class Rei(Pecas_protocol):

    def __init__(self, ):
        self._roque_feito = None
        self._first_play_king = True

        
    def movimento(pos_inicial: Casa) -> List:
        self._fist_play_king = False
        
    
    def is_valido(list: Casa) -> bool:
        pass

    def verificaTorre_isValid(self, torre : Torre) -> bool:
        return torre.first_play_torre()

    def is_safe(self) -> bool:
        pass

    def is_roque_valid(self):
        return self._first_play_king and self.verificaTorre_isValid() and self.is_safe()