from pecas_method_protocol import Pecas_protocol

class Cavalo(Pecas_protocol):

    def __init__(self) -> None:
        pass

    def movimento(pos_inicial: Casa) -> List:
        return super().movimento()
    
    def is_valido(list: Casa) -> bool:
        for i in range(len(casas)):
            for verifica in cassa[i]:
                if not verifica.get_pecas() is None:
                    return false
        return true
    