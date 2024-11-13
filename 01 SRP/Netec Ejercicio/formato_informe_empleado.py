""" Ejercicio de Netec - Clase FormatoInformeEmpleado """

from empleado import Empleado

class FormatoInformeEmpleado:
    """
    Clase que formatea los datos del empleado para generar un informe.
    """
    def formatear(self, empleado: Empleado) -> str:
        """
        Formatea los detalles del empleado en un informe.

        Args:
            empleado (Empleado): El empleado a formatear.

        Returns:
            str: El informe formateado del empleado.
        """
        return f"Informe del Empleado: {empleado.obtener_detalles()}"