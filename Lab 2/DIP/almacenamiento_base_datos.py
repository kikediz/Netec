from almacenamiento import Almacenamiento

class AlmacenamientoBaseDatos(Almacenamiento):
    def guardar(self, orden: str):
        print(f"Guardando {orden} en la base de datos")

    def obtener(self, id: str) -> str:
        return f"Orden {id} desde la base de datos"