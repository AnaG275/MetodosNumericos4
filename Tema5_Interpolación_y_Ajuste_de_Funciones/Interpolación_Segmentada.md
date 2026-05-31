# Interpolación Segmentada

## Definición
La Interpolación Segmentada es un método numérico que aproxima valores
desconocidos utilizando diferentes funciones en intervalos específicos
del conjunto de datos. En lugar de emplear un único polinomio para todos
los puntos, divide el dominio en segmentos y construye una función para
cada intervalo.

La forma más común consiste en aplicar interpolación lineal entre pares
consecutivos de puntos, obteniendo una aproximación más estable cuando se
trabaja con grandes cantidades de datos.

---

## Fórmula

Para un valor x perteneciente al intervalo [xᵢ, xᵢ₊₁]:

P(x) = yᵢ + [(yᵢ₊₁ - yᵢ)/(xᵢ₊₁ - xᵢ)] · (x - xᵢ)

Donde:
- xᵢ, xᵢ₊₁ → extremos del segmento
- yᵢ, yᵢ₊₁ → valores conocidos
- x         → punto a interpolar
- P(x)      → valor aproximado

Cada intervalo utiliza su propia ecuación de interpolación.

---

## Algoritmo

Definir el conjunto de puntos conocidos

Ordenar los puntos según los valores de x

Identificar el intervalo donde se encuentra el valor a interpolar

Seleccionar los dos puntos que forman dicho segmento

Calcular la pendiente del segmento

Aplicar la fórmula de interpolación lineal en ese intervalo

Obtener el valor aproximado

Mostrar el resultado

---

## Ejemplo

Datos:

| x | y |
|---|---|
| 0 | 1 |
| 2 | 5 |
| 4 | 9 |
| 6 | 13 |

Interpolar en:

x = 3

El valor pertenece al intervalo [2,4]

Usando los puntos:

(2,5) y (4,9)

P(3) = 5 + [(9-5)/(4-2)](3-2)

P(3) = 5 + (4/2)(1)

P(3) = 7

---

## Ejemplo y Caso de Prueba

**Caso de prueba:**

Datos:

| x | y |
|---|---|
| 1 | 2 |
| 3 | 6 |
| 5 | 10 |
| 7 | 14 |

Interpolar en x = 4

El valor pertenece al intervalo [3,5]

| Punto | x | y |
|--------|----|----|
| P₁ | 3 | 6 |
| P₂ | 5 | 10 |

**Resultado:** `P(4) = 8.0000`

---

**Ejercicio:**

Datos:

| x | y |
|---|---|
| 2 | 4 |
| 4 | 8 |
| 6 | 12 |
| 8 | 16 |

Interpolar en x = 7

El valor pertenece al intervalo [6,8]

| Punto | x | y |
|--------|----|----|
| P₂ | 6 | 12 |
| P₃ | 8 | 16 |

**Resultado:**
- Entrada: puntos = {(2,4), (4,8), (6,12), (8,16)}, x = 7
- Resultado esperado: 14.0000
- Resultado float:    14.0000
- Segmento utilizado: [6,8]
- Error acumulado:    0.0000
