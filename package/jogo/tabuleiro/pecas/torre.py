from pecas_method_protocol import Pecas_protocol
class Cavalo(Pecas_protocol):
    
    def __init__(self) -> None:
        self._first_play_torre = True
    
    def movimento(pos_inicial:Casa) -> List:
        self._first_play_torre = False
        pass

    def first_play_torre(self):
        return self._first_play_torre
    