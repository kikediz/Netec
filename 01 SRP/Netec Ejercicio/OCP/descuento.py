from abc import ABC, abstractmethod

class Descuento(ABC):
    @abstractmethod
    def calcular(self, monto: float) -> float:
        pass