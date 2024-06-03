from pecas_method_protocol import Pecas_protocol
from typing import List
<<<<<<< HEAD
from casa import Casa

class Cavalo(Pecas_protocol):

    def __init__(self) -> None:
        super().__init__()
        
    def movimento(self, pos_inicial: Casa) -> List:
        movimentos_possiveis = []
        
        #coordenadas do x e y
        direcao = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        for direcao_x, direcao_y in direcao:
            nova_posicao = Casa(pos_inicial.x + direcao_x, pos_inicial.y + direcao_y)
            if self.is_valido(nova_posicao):
                movimentos_possiveis.append(nova_posicao)
        
        return movimentos_possiveis
        

    def is_valido(self, casas: List[Casa]) -> bool:
        return super().is_valido(casas)

        
    

    
    
    
        
        
=======


class Cavalo(Pecas_protocol):

    def __init__(self) -> None:
        pass

    def movimento(pos_inicial: Casa) -> List:
        return super().movimento()
    
    def is_valido(list: Casa) -> bool:
        return super().is_valido()
        
>>>>>>> pecas
    