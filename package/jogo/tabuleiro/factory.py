from abc import ABC, abstractmethod

from pecas import piao, rainha, cavalo, torre, rei

class PecaFactory:
    def __init__(self):
        pass

    def criar_peca(self, linha, coluna):
        if(linha == 0):
            return self.criar_branca(coluna)
        if(linha == 1):
            return self.criar_branca(coluna)
        if(linha == 6):
            return self.criar_preta(coluna)
        elif linha == 7:
            return self.criar_preta(coluna)
        
    def criar_branca(self, coluna):
        if(coluna == 0 or 7):
            return Torre(True)
        if(coluna == 1 or 6):
            return Cavalo(True)
        if(coluna == 2 or 5):
            return Bispo(True)
        if(coluna == 3):
            return Rainha(True)
        else:  
            return Rei(True)
        
    def criar_preta(self, coluna):
        if(coluna == 0 or 7):
            return Torre(True)
        if(coluna == 1 or 6):
            return Cavalo(True)
        if(coluna == 2 or 5):
            return Bispo(True)
        if(coluna == 3):
            return Rainha(True)
        else:
            return Rei(True)
