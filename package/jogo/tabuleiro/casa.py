from pecas import Peca

class Casa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.set_peca()

    def get_peca(self, peca):
        if(peca != None):
            return peca
        else:
            return None
        
    def get_xy(self):
        return self.x, self.y
        
    def set_peca(self):
        pass