# Error de Precisión

## Definición
El Error de Precisión es una medida que permite evaluar qué tan cercana
es una aproximación respecto al valor exacto en términos porcentuales.
Se utiliza frecuentemente en métodos numéricos para determinar la calidad
de una aproximación y comparar diferentes resultados obtenidos.

Mientras menor sea el error de precisión, mayor será la exactitud del
resultado calculado.

---

## Fórmula

Error de Precisión (%) = (|Valor Exacto − Valor Aproximado| / |Valor Exacto|) × 100

Donde:
- Valor Exacto       → resultado real o teórico
- Valor Aproximado   → resultado obtenido mediante un método numérico
- | |                → valor absoluto
- 100                → convierte el resultado a porcentaje

---

## Algoritmo

Obtener el valor exacto

Obtener el valor aproximado

Calcular la diferencia entre ambos valores

Obtener el valor absoluto de la diferencia

Dividir la diferencia entre el valor exacto

Multiplicar el resultado por 100

Mostrar el porcentaje de error obtenido

Interpretar el resultado:
entre menor sea el porcentaje,
mayor será la precisión de la aproximación

---

## Ejemplo

Valor exacto = 50.0000

Valor aproximado = 49.5000

Error de Precisión (%) = (|50.0000 − 49.5000| / 50.0000) × 100

Error de Precisión (%) = (0.5000 / 50.0000) × 100

Error de Precisión (%) = 1.0000 %

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Valor exacto = 100.0000, valor aproximado = 98.5000

| Dato | Valor |
|-------|---------|
| Valor exacto | 100.0000 |
| Valor aproximado | 98.5000 |
| Diferencia absoluta | 1.5000 |
| Error de precisión (%) | 1.5000 |

**Resultado:** `Error de Precisión = 1.5000 %`

---

**Ejercicio:** Valor exacto = 3.141593, valor aproximado = 3.120000

| Dato | Valor |
|-------|---------|
| Valor exacto | 3.141593 |
| Valor aproximado | 3.120000 |
| Diferencia absoluta | 0.021593 |
| Error de precisión (%) | 0.6873 |

**Resultado:**
- Entrada: valor exacto = 3.141593, valor aproximado = 3.120000
- Resultado esperado: 0.6873 %
- Resultado float:    0.6873 %
- Diferencia absoluta: 0.021593
- Error acumulado:    0.0000 %
