from pecas_method_protocol import Pecas_protocol

class Bispo(Pecas_protocol):
    def movomento(self, pos_inicial: Casa) -> List[Casa]:
        movimentos_possiveis = []
        direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direcao in direcoes:
            for i in range(1, 8):
                novo_x = pos_inicial.x + direcao[0] * i
                novo_y = pos_inicial.y + direcao[1] * i

                if 0 <= novo_x < 8 and 0 <= novo_y < 8:
                    movimentos_possiveis.append(Casa(novo_x, novo_y))
                else:
                    break
        return movimentos_possiveis
    
    def is_valido(self, caminho: List[Casa]) -> bool:
        if len(caminho)<2:
            return False

        delta_x = abs(caminho[1].x - caminho[0].x)
        delta_y = abs(caminho[1].y - caminho[0].y)

        if delta_x == delta_y:
            for i in range(1, len(caminho)):
                if abs(caminho[i].x - caminho[i-1].x) != 1 or abs(caminho[i].y - caminho[i-1].y) != 1:
                    return False
            return True
        
        return False