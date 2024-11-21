class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        self.bonus = 0

    def calcular_bonus(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def calcular_salario(self):
        self.bonus = self.calcular_bonus()
        return self.salario + self.bonus

    def imprimir_detalles(self):
        print(f"Empleado: {self.nombre}, Salario: {self.salario}, Bonus: {self.bonus}")

class Gerente(Empleado):
    def calcular_bonus(self):
        return self.salario * 0.20

class Director(Empleado):
    def calcular_bonus(self):
        return self.salario * 0.30

class EmpleadoRegular(Empleado):
    def calcular_bonus(self):
        return self.salario * 0.10