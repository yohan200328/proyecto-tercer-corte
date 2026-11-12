# Registro de Cambios (CHANGELOG) - Módulo de Envíos (EnvíaYa)

Todas las modificaciones notables de este proyecto siguen los principios de Versionado Semántico (SemVer).

## [2.0.0] - 2026-11-11
### Añadido
- Implementación del **Patrón Estrategia (Strategy Pattern)** mediante la interfaz `ZonaStrategy` y clases concretas para desacoplar los recargos geográficos (`UrbanaStrategy`, `RuralStrategy`, `NacionalStrategy`).
- Función matemática estándar de redondeo al múltiplo de $100 más cercano (`redondear_centena`).
- Suite completa de casos de prueba automatizados en `pytest` con cobertura del 100%.

### Cambiado
- Reemplazo de todos los números mágicos por constantes globales con nombres descriptivos (`TARIFA_TRAMO_1`, `VALOR_KG_ADICIONAL`, etc.).
- Modificación del límite de fin de semana a `d >= 6` para incluir correctamente los sábados y domingos.
- Ajuste del orden de ejecución del recargo temporal de fin de semana para aplicarse estrictamente *después* de los descuentos (Regla $E=1$).

### Corregido (Mantenimiento Correctivo)
- **DEF-01:** Agregada validación estricta de rangos y tipos para días y zonas de envío.
- **DEF-02 y DEF-03:** Solucionado el error de cálculo en días sábado y la precedencia matemática de recargos.
- **DEF-04:** Corregido el truncamiento entero por un redondeo comercial correcto.
- **DEF-05:** Eliminación de literales fijos para el parámetro de peso máximo (`PMAX`).

---

## [1.0.0] - 2026-11-01
### Versión Inicial (Heredada)
- Versión base del sistema (`envios.py`) desarrollada por el equipo heredado con 5 defectos críticos iniciales y una complejidad ciclomática de $V(G) = 14$.