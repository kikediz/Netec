""" Ejercicio de Netec - Clase GeneradorInformeEmpleado """

from empleado import Empleado
from formato_informe_empleado import FormatoInformeEmpleado

class GeneradorInformeEmpleado:
    """
    Clase que genera informes para empleados.
    """
    def __init__(self, empleado: Empleado, formateador: FormatoInformeEmpleado):
        self.empleado = empleado
        self.formateador = formateador

    def generar_informe(self):
        """
        Genera un informe del empleado.

        Returns:
            str: El informe del empleado.
        """
        return self.formateador.formatear(self.empleado)