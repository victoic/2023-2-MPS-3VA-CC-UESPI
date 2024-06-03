from typing import List, Any
from transformavel import Transformavel
from pecas_method_protocol import Pecas_protocol
import sys
import os
sys.path.append(os.path.abspath( '../casa'))
from casa import Casa



class Piao(Transformavel, Pecas_protocol):
    def __init__(self) -> None:
         pass
     
     
     #Any será substituido Casa
    def movimentos(self, pos_inicial : Any) -> List:
         pass
    
     #Any será substituido Casa
    def is_valido(list: Any) -> bool:
        for i in range(len(casas)):
            for verifica in cassa[i]:
                if not verifica.get_pecas() is None:
                    return false
        return true
    
    def transformar(self) -> Peca:
        
        peca = input("Digite para qual peça você deseja trocar, 1 - Rainha, 2 - Torre, 3 - Bispo, 4 - Cavalo: ")

        if peca == '1':
            return Rainha()
        elif peca == '2':
            return Torre()
        elif peca == '3':
            return Bispo()
        elif peca == '4':
            return cavalo()
        else:
            print("Opção inválida, escolha uma opção valida por favor")
            return self.transformar()

