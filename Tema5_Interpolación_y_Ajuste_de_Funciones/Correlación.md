# Correlación

## Definición
La Correlación es una medida estadística que permite determinar el grado
de relación existente entre dos variables. Indica si ambas variables
tienden a aumentar juntas, disminuir juntas o comportarse de manera
independiente.

El coeficiente de correlación toma valores entre -1 y 1:
- r = 1   → correlación positiva perfecta
- r = 0   → no existe correlación lineal
- r = -1  → correlación negativa perfecta

Mientras más cercano sea el valor a ±1, más fuerte será la relación entre
las variables.

---

## Fórmula

Coeficiente de Correlación de Pearson:

r = [ nΣ(xy) − (Σx)(Σy) ]
    ─────────────────────
    √[(nΣx² − (Σx)²)(nΣy² − (Σy)²)]

Donde:
- r      → coeficiente de correlación
- n      → número de datos
- Σxy    → suma de los productos x·y
- Σx     → suma de los valores de x
- Σy     → suma de los valores de y
- Σx²    → suma de los cuadrados de x
- Σy²    → suma de los cuadrados de y

---

## Algoritmo

Definir los conjuntos de datos X y Y

Contar el número de observaciones n

Calcular Σx y Σy

Calcular Σxy

Calcular Σx² y Σy²

Sustituir los valores en la fórmula de Pearson

Calcular el coeficiente de correlación r

Interpretar el resultado obtenido

Determinar si la correlación es positiva,
negativa o inexistente

---

## Ejemplo

Datos:

X = [1, 2, 3, 4, 5]

Y = [2, 4, 6, 8, 10]

Tabla de cálculo:

| x | y | xy | x² | y² |
|---|---|----|----|----|
| 1 | 2 | 2  | 1  | 4  |
| 2 | 4 | 8  | 4  | 16 |
| 3 | 6 | 18 | 9  | 36 |
| 4 | 8 | 32 | 16 | 64 |
| 5 |10 | 50 | 25 |100 |

Resultado:

r = 1.0000

Existe una correlación positiva perfecta.

---

## Ejemplo y Caso de Prueba

**Caso de prueba:**

X = [1, 2, 3, 4]

Y = [3, 5, 7, 9]

| Dato | Valor |
|--------|---------|
| n | 4 |
| Σx | 10 |
| Σy | 24 |
| Σxy | 70 |
| Σx² | 30 |
| Σy² | 164 |

**Resultado:** `r = 1.0000`

---

**Ejercicio:**

X = [2, 4, 6, 8, 10]

Y = [5, 7, 9, 11, 13]

| Dato | Valor |
|--------|---------|
| n | 5 |
| Σx | 30 |
| Σy | 45 |
| Σxy | 310 |
| Σx² | 220 |
| Σy² | 445 |

**Resultado:**
- Entrada: X = [2,4,6,8,10], Y = [5,7,9,11,13]
- Resultado esperado: r = 1.0000
- Resultado float:    r = 1.0000
- Tipo de correlación: Positiva perfecta
- Error acumulado:    0.0000
