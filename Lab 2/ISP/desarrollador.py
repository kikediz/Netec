from interfaces import Trabajador, Descansador, Reportador

class Desarrollador(Trabajador, Descansador, Reportador):
    def trabajar(self):
        return "Desarrollador trabajando"

    def tomar_descanso(self):
        return "Desarrollador tomando un descanso"

    def reportar(self):
        return "Desarrollador reportando el progreso"