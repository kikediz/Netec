from procesador_ordenes import ProcesadorOrdenes
from almacenamiento_base_datos import AlmacenamientoBaseDatos
from almacenamiento_archivo import AlmacenamientoArchivo

# Uso
if __name__ == "__main__":
    # Puedes cambiar fácilmente la implementación de almacenamiento aquí
    almacenamiento = AlmacenamientoBaseDatos()
    # almacenamiento = AlmacenamientoArchivo()

    procesador = ProcesadorOrdenes(almacenamiento)
    procesador.procesar("Orden #1")