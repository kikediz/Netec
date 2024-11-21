from descuento import Descuento

class DescuentoRegular(Descuento):
    def calcular(self, monto: float) -> float:
        return monto * 0.9  # 10% de descuento