""" Ejercicio de Netec """


class Empleado:
    """
    Clase que representa a un empleado.
    """
    def __init__(self, nombre: str, puesto: str, salario: float):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def obtener_detalles(self):
        """
        Obtiene los detalles del empleado.

        Returns:
            str: Una cadena con el nombre, puesto y salario del empleado.
        """
        return f"{self.nombre}, {self.puesto}, Salario: {self.salario}"


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


# Uso
if __name__ == "__main__":
    empleado = Empleado("Rodrigo Silva", "Ingeniero de Software", 90000)
    formateador = FormatoInformeEmpleado()
    generador_informe = GeneradorInformeEmpleado(empleado, formateador)
    informe = generador_informe.generar_informe()
    print(informe)