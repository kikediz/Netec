from descuento import Descuento

class DescuentoEstudiante(Descuento):
    def calcular(self, monto: float) -> float:
        return monto * 0.8  # 20% de descuento