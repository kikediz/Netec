from descuento import Descuento

class DescuentoSenior(Descuento):
    def calcular(self, monto: float) -> float:
        return monto * 0.7  # 30% de descuento