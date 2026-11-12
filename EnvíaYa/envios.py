from abc import ABC, abstractmethod

# Constantes de Negocio (Eliminación de números mágicos)
TARIFA_TRAMO_1 = 6000
TARIFA_TRAMO_2 = 9000
VALOR_KG_ADICIONAL = 800
COSTO_MINIMO = 5000
RECARGO_FINDE = 2000

# Interfaz Estrategia para Zonas (Patrón Estrategia)
class ZonaStrategy(ABC):
    @abstractmethod
    def calcular_recargo(self, tarifa_base: float) -> float:
        pass

class UrbanaStrategy(ZonaStrategy):
    def calcular_recargo(self, tarifa_base: float) -> float:
        return tarifa_base

class RuralStrategy(ZonaStrategy):
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje
    def calcular_recargo(self, tarifa_base: float) -> float:
        return tarifa_base + (tarifa_base * self.porcentaje)

class NacionalStrategy(ZonaStrategy):
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje
    def calcular_recargo(self, tarifa_base: float) -> float:
        return tarifa_base + (tarifa_base * self.porcentaje)

# Función de Redondeo Matemática Correcta (R8)
def redondear_centena(valor: float) -> int:
    residuo = valor % 100
    if residuo >= 50:
        return int(valor + (100 - residuo))
    else:
        return int(valor - residuo)

# Función principal refactorizada (v2.0.0)
def calc(p: float, z: str, c: str, d: int, cup: str = None, pmax: int = 50, l1: int = 3, l2: int = 10, rr: float = 0.15, rn: float = 0.50, desc_vip: float = 0.15) -> int:
    if p <= 0 or p > pmax:
        raise ValueError("peso invalido")
    if d < 1 or d > 7:
        raise ValueError("dia invalido")
        
    # 1. Tarifa Base según Tramos
    if p <= l1:
        t = TARIFA_TRAMO_1
    elif p <= l2:
        t = TARIFA_TRAMO_2
    else:
        t = TARIFA_TRAMO_2 + (p - l2) * VALOR_KG_ADICIONAL
        
    # 2. Aplicación de Estrategia por Zona
    estrategias_zona = {
        "urbana": UrbanaStrategy(),
        "rural": RuralStrategy(rr),
        "nacional": NacionalStrategy(rn)
    }
    if z not in estrategias_zona:
        raise ValueError("zona invalida")
    t = estrategias_zona[z].calcular_recargo(t)
    
    # 3. Descuentos de Cliente y Cupón (B=1: Sucesivos)
    if c == "frecuente":
        t = t - (t * 0.05)
    elif c == "vip":
        t = t - (t * desc_vip)
    elif c != "normal":
        raise ValueError("cliente invalido")
        
    if cup == "ENVIO10":
        t = t - (t * 0.10)
    elif cup is not None:
        pass  # F=8: Se ignora cupón inexistente
        
    # 4. Recargo de Fin de Semana (E=1: Después de descuentos, d >= 6 cubre sábado y domingo)
    if d >= 6:
        t = t + RECARGO_FINDE
        
    # 5. Piso Mínimo y Redondeo Estándar
    if t < COSTO_MINIMO:
        t = COSTO_MINIMO
        
    return redondear_centena(t)