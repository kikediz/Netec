from almacenamiento import Almacenamiento

class ProcesadorOrdenes:
    def __init__(self, almacenamiento: Almacenamiento):
        self.almacenamiento = almacenamiento

    def procesar(self, orden: str):
        print(f"Procesando {orden}")
        self.almacenamiento.guardar(orden)