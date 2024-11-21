from descuento import Descuento
from descuento_estudiante import DescuentoEstudiante
from descuento_senior import DescuentoSenior
from descuento_regular import DescuentoRegular
from sin_descuento import SinDescuento

class CalculadoraDescuento:
    def calcular(self, descuento: Descuento, monto: float) -> float:
        return descuento.calcular(monto)

# Uso
if __name__ == "__main__":
    calculadora = CalculadoraDescuento()
    
    descuento_estudiante = DescuentoEstudiante()
    total_estudiante = calculadora.calcular(descuento_estudiante, 100)
    print(f"Total con descuento para estudiante: {total_estudiante}")
    
    descuento_senior = DescuentoSenior()
    total_senior = calculadora.calcular(descuento_senior, 100)
    print(f"Total con descuento para senior: {total_senior}")
    
    descuento_regular = DescuentoRegular()
    total_regular = calculadora.calcular(descuento_regular, 100)
    print(f"Total con descuento para cliente regular: {total_regular}")
    
    sin_descuento = SinDescuento()
    total_sin_descuento = calculadora.calcular(sin_descuento, 100)
    print(f"Total sin descuento: {total_sin_descuento}")