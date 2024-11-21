from abc import ABC, abstractmethod

class Almacenamiento(ABC):
    @abstractmethod
    def guardar(self, orden: str):
        pass

    @abstractmethod
    def obtener(self, id: str) -> str:
        pass