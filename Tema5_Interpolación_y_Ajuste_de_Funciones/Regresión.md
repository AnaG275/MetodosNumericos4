# Regresión Lineal

## Definición
La Regresión Lineal es un método numérico y estadístico que permite encontrar
una ecuación matemática que describa la relación entre dos variables. Su objetivo
es ajustar una recta a un conjunto de datos experimentales de manera que la suma
de los errores al cuadrado entre los valores observados y los valores estimados
sea mínima.

Este método es ampliamente utilizado para analizar tendencias, realizar
predicciones y modelar fenómenos donde existe una relación aproximadamente lineal
entre las variables.

---

## Fórmula

**Ecuación de la recta de regresión:**

    y = a + bx

**Pendiente:**

    b = (nΣxy − ΣxΣy) / (nΣx² − (Σx)²)

**Intercepto:**

    a = (Σy − bΣx) / n

Donde:
- a → intercepto de la recta
- b → pendiente de la recta
- n → número de observaciones
- x → variable independiente
- y → variable dependiente
- Σxy → suma de los productos x·y
- Σx² → suma de los cuadrados de x

---

## Algoritmo

Ingresar los datos experimentales (x, y)

Calcular las sumatorias:
- Σx
- Σy
- Σxy
- Σx²

Determinar la pendiente b mediante la fórmula

Calcular el intercepto a

Construir la ecuación de regresión:

    y = a + bx

Evaluar la ecuación para estimar nuevos valores

Mostrar la recta obtenida y las predicciones

---

## Ejemplo

Datos experimentales:

| x | y |
|---|---|
| 1 | 3 |
| 2 | 5 |
| 3 | 7 |
| 4 | 9 |
| 5 | 11 |

Cálculos:

    Σx  = 15
    Σy  = 35
    Σxy = 125
    Σx² = 55
    n   = 5

Pendiente:

    b = (5·125 − 15·35) / (5·55 − 15²)
    b = 100 / 50
    b = 2

Intercepto:

    a = (35 − 2·15) / 5
    a = 1

Recta de regresión:

    y = 1 + 2x

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Datos experimentales

| x | y | xy | x² |
|---|---|----|----|
| 1 | 3 | 3  | 1  |
| 2 | 5 | 10 | 4  |
| 3 | 7 | 21 | 9  |
| 4 | 9 | 36 | 16 |
| 5 |11 | 55 | 25 |

| Σx | Σy | Σxy | Σx² |
|----|----|-----|-----|
| 15 | 35 | 125 | 55 |

Recta obtenida:

    y = 1 + 2x

Estimación para x = 6:

    y = 1 + 2(6)
    y = 13

**Ejercicio:** Datos de producción

| x | y |
|---|---|
| 1 | 8  |
| 2 | 11 |
| 3 | 14 |
| 4 | 17 |
| 5 | 20 |

| x | y | xy | x² |
|---|---|----|----|
| 1 | 8  | 8  | 1  |
| 2 |11  |22  | 4  |
| 3 |14  |42  | 9  |
| 4 |17  |68  |16  |
| 5 |20  |100 |25  |

    Σx  = 15
    Σy  = 70
    Σxy = 240
    Σx² = 55

    b = (5·240 − 15·70) / (5·55 − 15²)
    b = 150 / 50
    b = 3

    a = (70 − 3·15) / 5
    a = 5

Recta obtenida:

    y = 5 + 3x

Estimación para x = 6:

    y = 5 + 3(6)
    y = 23

**Resultado:**
- Entrada: datos experimentales de producción
- Pendiente: 3.0000
- Intercepto: 5.0000
- Ecuación obtenida: y = 5 + 3x
- Valor estimado para x = 6: 23.0000
- Error de ajuste: mínimo por método de mínimos cuadrados
