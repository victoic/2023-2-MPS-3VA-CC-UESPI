from pecas_method_protocol import Pecas_protocol

class Rainha(Pecas_protocol):

    def __init__(self) -> None:
        super().__init__()

    def movimento(pos_inicial: Casa) -> List:
        return super().movimento()
    
    def is_valido(list: Casa) -> bool:
        return super().is_valido()