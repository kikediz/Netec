from interfaces import Trabajador, Reportador

class Gerente(Trabajador, Reportador):
    def trabajar(self):
        return "Gerente trabajando"
    
    def tomar_descanso(self): 
        return "Gerente Estoy tomando un descanso"

    def reportar(self):
        return "Gerente reportando el progreso"