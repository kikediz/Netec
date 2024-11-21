from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Descansador(ABC):
    @abstractmethod
    def tomar_descanso(self):
        pass

class Reportador(ABC):
    @abstractmethod
    def reportar(self):
        pass