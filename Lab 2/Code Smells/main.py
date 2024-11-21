from empleado import Gerente, Director, EmpleadoRegular
from repositorio_empleado import RepositorioEmpleado

def main():
    # Crear empleados
    gerente = Gerente("Gerente de Ventas", 5000)
    director = Director("Director de Marketing", 7000)
    empleado_regular = EmpleadoRegular("Empleado de Soporte", 3000)

    # Calcular salarios
    gerente.calcular_salario()
    director.calcular_salario()
    empleado_regular.calcular_salario()

    # Imprimir detalles
    gerente.imprimir_detalles()
    director.imprimir_detalles()
    empleado_regular.imprimir_detalles()

    # Guardar en base de datos
    repositorio = RepositorioEmpleado()
    repositorio.guardar(gerente)
    repositorio.guardar(director)
    repositorio.guardar(empleado_regular)

if __name__ == "__main__":
    main()