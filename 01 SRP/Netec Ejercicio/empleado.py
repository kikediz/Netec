""" Ejercicio de Netec - Clase Empleado """


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