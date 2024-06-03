
from random import random
from tabuleiro.tabuleiro import Tabuleiro
# from tabuleiro.casa import Casa
from TimeoutInput import input_com_tempo

class Jogo:

  TEMPO_JOGADA = 60*3
  def __new__(cls, is_blitz = False):
    
    if not hasattr(cls,"jogo"):
      cls.jogo = super(Jogo, cls).__new__(cls)
      cls.id = random()*10 //1
      cls._is_blitz = is_blitz  

    return cls.jogo
  
  def __init__(self, is_blitz = False) -> None:
    self._tempo_jogador1 = Jogo.TEMPO_JOGADA
    self._tempo_jogador2 = Jogo.TEMPO_JOGADA
    self._turno_atual = 1
    self._contador_turnos = 1
    self._tabuleiro = Tabuleiro()

  # TODO: implementar
  def is_fim(self) -> bool:
    return False

  #TODO: implementar
  def mover(self, origem, destino) -> bool:
    pass

  #TODO: implementar
  def is_xeque(self) -> bool:
    pass

  def main(self):
  
    while not self.is_fim():
      
      movimento = self.pegar_movimento()

      # movimento inválido
      # ou encerrou o tempo de jogada se for jogo blitz
      if movimento == None:
        self.atualizar_turno()
        continue

      (origem, destino) = movimento

      self.mover(origem,destino)

  def pegar_movimento(self):
    texto = f"turno do player {self._contador_turnos}."
    texto += "Selecione uma peça e uma casa de destino no formato:"
    texto += "\ncasa da peça : casa de destino"
    texto += "\n0,0 : 1,1\n"
    
    # se for blitz ele pede a jogada com tempo limite
    # se não é por input normal 

    if self._is_blitz:
      try:
        movimento = input_com_tempo(texto, self._tempo_jogador1)
      except:
        print("Acabou seu Tempo! É a vez do outro jogador")
        return None
    
    else:
      movimento = input(texto)
    
    (posicao_origem, posicao_destino) = movimento.replace(" ","").split(":") 
    
    posicao_destino = posicao_destino.split(",")
    posicao_origem = posicao_origem.split(",")

    x = int(posicao_origem[0])
    y = int(posicao_origem[1]) 
    origem = (x,y)
    
  
    #TODO:implementar pegar a casa de origem


    x = int(posicao_destino[0])
    y = int(posicao_destino[1])
    destino = (x,y)
    #TODO:implementar pegar a casa de destino
    
    return (origem, destino)
  
  def atualizar_turno(self):

    self._contador_turnos = 2 if self._contador_turnos == 1 else 1
    self._turno_atual+=1


