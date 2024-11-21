from almacenamiento import Almacenamiento

class AlmacenamientoArchivo(Almacenamiento):
    def guardar(self, orden: str):
        print(f"Guardando {orden} en un archivo")

    def obtener(self, id: str) -> str:
        return f"Orden {id} desde un archivo"