# Error de Truncamiento

## Definición
El Error de Truncamiento ocurre cuando un procedimiento matemático infinito
se sustituye por una versión finita para facilitar los cálculos. Este tipo
de error aparece frecuentemente en métodos numéricos al aproximar derivadas,
integrales, series infinitas o ecuaciones diferenciales.

A diferencia del error de redondeo, el error de truncamiento no se produce
por limitar decimales, sino por omitir términos o pasos de un proceso
matemático exacto.

---

## Fórmula

Error de Truncamiento = |Valor Exacto − Valor Aproximado|

Donde:
- Valor Exacto         → resultado matemático real
- Valor Aproximado     → resultado obtenido mediante una aproximación
- | |                  → valor absoluto

---

## Algoritmo

Obtener el valor exacto del problema

Aplicar un método de aproximación

Calcular el resultado aproximado

Restar el valor aproximado al valor exacto

Obtener el valor absoluto de la diferencia

Mostrar el error obtenido

Interpretar el resultado:
entre menor sea el error de truncamiento,
mejor será la aproximación utilizada

---

## Ejemplo

Aproximar:

e ≈ 1 + 1 + 1/2

Valor aproximado:

e ≈ 2.5000

Valor exacto:

e = 2.718281828

Error de Truncamiento:

|2.718281828 − 2.5000|

= 0.218281828

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Aproximación de sen(0.5) usando los dos primeros términos de la serie de Taylor

sen(x) ≈ x

| Dato | Valor |
|-------|---------|
| Valor exacto | 0.479426 |
| Valor aproximado | 0.500000 |
| Diferencia | 0.020574 |
| Error de truncamiento | 0.020574 |

**Resultado:** `Error de Truncamiento = 0.020574`

---

**Ejercicio:** Aproximar eˣ para x = 1 usando:

e¹ ≈ 1 + 1 + 1²/2

| Dato | Valor |
|-------|---------|
| Valor exacto | 2.718282 |
| Valor aproximado | 2.500000 |
| Diferencia | 0.218282 |
| Error de truncamiento | 0.218282 |

**Resultado:**
- Entrada: e¹ ≈ 1 + 1 + 1²/2
- Resultado esperado: 0.218282
- Resultado float:    0.218282
- Diferencia:         0.218282
- Error acumulado:    0.000000
