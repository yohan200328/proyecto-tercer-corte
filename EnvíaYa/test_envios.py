import pytest
from envios import calc

# Casos de validación de peso (R1)
def test_cp01_peso_cero():
    with pytest.raises(ValueError, match="peso invalido"):
        calc(0, "urbana", "normal", 1)

def test_cp02_peso_negativo():
    with pytest.raises(ValueError, match="peso invalido"):
        calc(-1, "urbana", "normal", 1)

def test_cp09_peso_mayor_pmax():
    with pytest.raises(ValueError, match="peso invalido"):
        calc(50.01, "urbana", "normal", 1)

# Casos de validación de zona y día (R2)
def test_cp19_zona_insular_no_soportada_v1():
    with pytest.raises(ValueError):
        calc(4, "insular", "normal", 1)

def test_cp20_dia_mayor_siete():
    with pytest.raises(ValueError):
        calc(4, "urbana", "normal", 8)

def test_cp23_dia_cero():
    with pytest.raises(ValueError):
        calc(4, "urbana", "normal", 0)

def test_cp24_zona_inexistente():
    with pytest.raises(ValueError):
        calc(4, "interplanetaria", "normal", 1)

# Casos de tarifa base y límites (R3)
def test_cp03_peso_limite_inferior_valido():
    assert calc(0.01, "urbana", "normal", 1) == 6000

def test_cp04_peso_limite_L1_incluido():
    assert calc(3, "urbana", "normal", 1) == 6000

def test_cp05_peso_despues_L1():
    assert calc(3.01, "urbana", "normal", 1) == 9000

def test_cp06_peso_limite_L2():
    assert calc(10, "urbana", "normal", 1) == 9000

def test_cp07_peso_despues_L2_redondeo():
    assert calc(10.01, "urbana", "normal", 1) == 9000

def test_cp08_peso_limite_PMAX():
    assert calc(50, "urbana", "normal", 1) == 41000

# Casos de recargos por zona (R4)
def test_cp10_zona_rural_redondeo():
    assert calc(4, "rural", "normal", 1) == 10400

def test_cp11_zona_nacional():
    assert calc(4, "nacional", "normal", 1) == 13500

# Casos de fin de semana y orden de recargo (R5)
def test_cp14_sabado_sin_descuento():
    assert calc(4, "urbana", "normal", 6) == 11000

def test_cp15_domingo_con_cupon():
    assert calc(4, "urbana", "normal", 7, cup="ENVIO10") == 10100

# Casos de descuentos y combinación (R6)
def test_cp12_cliente_frecuente_redondeo():
    assert calc(4, "urbana", "frecuente", 1) == 8600

def test_cp13_rural_vip_redondeo():
    assert calc(4, "rural", "vip", 1) == 8800

def test_cp16_vip_y_cupon_encadenados():
    assert calc(4, "urbana", "vip", 1, cup="ENVIO10") == 6900

def test_cp17_combinacion_completa_sabado():
    assert calc(4, "rural", "vip", 6, cup="ENVIO10") == 9900

# Casos de cupón inexistente (R7) y mínimo (R8)
def test_cp18_cupon_inexistente_ignorado():
    assert calc(4, "urbana", "normal", 1, cup="DESC2026") == 9000

def test_cp21_costo_minimo_aplicado():
    assert calc(0.1, "urbana", "vip", 1, cup="ENVIO10") == 5000

def test_cp22_redondeo_hacia_arriba_50():
    assert calc(4, "urbana", "frecuente", 1) == 8600