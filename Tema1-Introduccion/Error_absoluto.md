# Error Absoluto

## Definición
El Error Absoluto es una medida utilizada para determinar la diferencia
entre un valor exacto o verdadero y un valor aproximado obtenido mediante
un cálculo, medición o método numérico.

Este error indica qué tan lejos se encuentra el resultado aproximado del
valor real, sin considerar si la diferencia es positiva o negativa.

---

## Fórmula

Error Absoluto = | Valor Exacto − Valor Aproximado |

Donde:
- Valor Exacto       → resultado real o teórico
- Valor Aproximado   → resultado obtenido mediante un método numérico
- | |                → valor absoluto

---

## Algoritmo

Obtener el valor exacto

Obtener el valor aproximado

Restar el valor aproximado al valor exacto

Calcular el valor absoluto de la diferencia

Mostrar el error obtenido

Interpretar el resultado:
entre más pequeño sea el error absoluto,
más precisa es la aproximación

---

## Ejemplo

Valor exacto = 3.141593

Valor aproximado = 3.140000

Error Absoluto = |3.141593 − 3.140000|

Error Absoluto = |0.001593|

Error Absoluto = 0.001593

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Valor exacto = 2.718282, valor aproximado = 2.710000

| Dato | Valor |
|-------|---------|
| Valor exacto | 2.718282 |
| Valor aproximado | 2.710000 |
| Diferencia | 0.008282 |
| Error absoluto | 0.008282 |

**Resultado:** `Error Absoluto = 0.008282`

---

**Ejercicio:** Valor exacto = 1.414214, valor aproximado = 1.410000

| Dato | Valor |
|-------|---------|
| Valor exacto | 1.414214 |
| Valor aproximado | 1.410000 |
| Diferencia | 0.004214 |
| Error absoluto | 0.004214 |

**Resultado:**
- Entrada: valor exacto = 1.414214, valor aproximado = 1.410000
- Resultado esperado: 0.004214
- Resultado float:    0.004214
- Diferencia:         0.004214
- Error acumulado:    0.000000
