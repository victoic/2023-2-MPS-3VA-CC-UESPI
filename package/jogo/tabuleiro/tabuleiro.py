from casa import Casa
class Tabuleiro:
    _instance = None #Variável que armazena a única instancia da classe tabuleiro


    def __new__(cls): #Criando uma nova instancia
        if cls._instance is None:
            cls._instance = super(Tabuleiro, cls).__new__(cls)
            cls._instance.__init__tabuleiro()
        return cls._instance
     
    def __init__tabuleiro(self) -> None:
        self.casas = [[Casa(x,y) for y in range(8)] for x in range(8)] #lista de listas contém uma matriz 8x8


    def get_pecas(self): #Manupulação do tabueleiro
        pecas =[]  #Lista de peças inicilaizada com lista vazia
        for row in self.casas: #percorre todas as casas do tabuleiro
            for casa in row:
                    if casa.get_peca:
                         pecas.append(casa.get_peca())
        return pecas  #retornar a lista de peças encontradas no tabuleiro
    def get_xy(self, x, y, peca):
         #acessa a casa na posição x e y na matriz
         self.casas[x][y].set_peca(peca)


     #Visualização do tabuleiro em string    
    def __reprCasas__(self):
         return f"Tabuleiro({self.casas})"