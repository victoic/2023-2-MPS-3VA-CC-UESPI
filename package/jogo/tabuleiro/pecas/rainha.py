from pecas_method_protocol import Pecas_protocol

class Rainha(Pecas_protocol):

    def __init__(self) -> None:
        super().__init__()

    def movimento(pos_inicial: Casa) -> List:

        movimentos_possiveis = []

        for i in range(8):
            if i != x:
                movimentos_possiveis.append((i, y))

        for j in range(8):
            if j != y:
                movimentos_possiveis.append((x, j))

 
        for i in range(1, 8):

            if x + i < 8 and y + i < 8:
                movimentos_possiveis.append((x + i, y + i))

            if x + i < 8 and y - i >= 0:
                movimentos_possiveis.append((x + i, y - i))

            if x - i >= 0 and y + i < 8:
                movimentos_possiveis.append((x - i, y + i))
        
            if x - i >= 0 and y - i >= 0:
                movimentos_possiveis.append((x - i, y - i))

        return movimentos_possiveis

    
    def is_valido(list: Casa) -> bool:
        for i in range(len(casas)):
            for verifica in cassa[i]:
                if not verifica.get_pecas() is None:
                    return false
        return true
