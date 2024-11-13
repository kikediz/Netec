""" Ejercicio de Netec - Main """

from empleado import Empleado
from formato_informe_empleado import FormatoInformeEmpleado
from generador_informe_empleado import GeneradorInformeEmpleado

if __name__ == "__main__":
    empleado = Empleado("Rodrigo Silva", "Ingeniero de Software", 90000)
    formateador = FormatoInformeEmpleado()
    generador_informe = GeneradorInformeEmpleado(empleado, formateador)
    informe = generador_informe.generar_informe()
    print(informe)