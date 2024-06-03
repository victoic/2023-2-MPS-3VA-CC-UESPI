from abc import ABC, abstractmethod

class Transformavel(ABC):

  @abstractmethod
  def transformar(self) -> Peca:
    pass