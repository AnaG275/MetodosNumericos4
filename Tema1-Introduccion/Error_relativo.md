# Error Relativo

## Definición
El Error Relativo es una medida que expresa qué tan grande es el error
absoluto en comparación con el valor exacto. A diferencia del error
absoluto, este error considera la magnitud del valor real, permitiendo
evaluar la precisión de una aproximación de forma proporcional.

Es ampliamente utilizado en métodos numéricos para comparar resultados
obtenidos en diferentes escalas.

---

## Fórmula

Error Relativo = |Valor Exacto − Valor Aproximado| / |Valor Exacto|

Donde:
- Valor Exacto       → resultado real o teórico
- Valor Aproximado   → resultado obtenido mediante un método numérico
- | |                → valor absoluto

---

## Algoritmo

Obtener el valor exacto

Obtener el valor aproximado

Calcular la diferencia entre ambos valores

Obtener el valor absoluto de la diferencia

Dividir la diferencia entre el valor exacto

Mostrar el valor obtenido

Interpretar el resultado:
entre más cercano sea a cero,
más precisa será la aproximación

---

## Ejemplo

Valor exacto = 25.0000

Valor aproximado = 24.5000

Error Relativo = |25.0000 − 24.5000| / 25.0000

Error Relativo = 0.5000 / 25.0000

Error Relativo = 0.0200

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Valor exacto = 12.5000, valor aproximado = 12.2000

| Dato | Valor |
|-------|---------|
| Valor exacto | 12.5000 |
| Valor aproximado | 12.2000 |
| Error absoluto | 0.3000 |
| Error relativo | 0.0240 |

**Resultado:** `Error Relativo = 0.0240`

---

**Ejercicio:** Valor exacto = 2.718282, valor aproximado = 2.700000

| Dato | Valor |
|-------|---------|
| Valor exacto | 2.718282 |
| Valor aproximado | 2.700000 |
| Error absoluto | 0.018282 |
| Error relativo | 0.0067 |

**Resultado:**
- Entrada: valor exacto = 2.718282, valor aproximado = 2.700000
- Resultado esperado: 0.0067
- Resultado float:    0.0067
- Error absoluto:     0.018282
- Error acumulado:    0.0000
