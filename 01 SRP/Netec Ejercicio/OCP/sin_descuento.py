from descuento import Descuento

class SinDescuento(Descuento):
    def calcular(self, monto: float) -> float:
        return monto  # Sin descuento