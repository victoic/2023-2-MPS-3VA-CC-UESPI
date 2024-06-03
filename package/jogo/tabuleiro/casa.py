from pecas import Peca

class Casa:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_peca(self):
        if(self != None):
            return self
        else:
            return None