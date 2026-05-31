# Regla de los 3 Puntos

## Definición
La Regla de los 3 Puntos es un método de diferenciación numérica utilizado
para estimar la derivada de una función a partir de valores cercanos al punto
de interés. Emplea un punto anterior, el punto donde se desea calcular la
derivada y un punto posterior, obteniendo una aproximación más precisa que
otros métodos basados únicamente en diferencias hacia adelante o hacia atrás.

Este procedimiento es ampliamente utilizado cuando se dispone de datos
experimentales o cuando la derivada analítica de la función es difícil de obtener.

---

## Fórmula

**Diferencia centrada de tres puntos:**

f'(x) ≈ (f(x+h) − f(x−h)) / (2h)

Donde:

- f'(x) = derivada aproximada en el punto x
- h = tamaño del incremento
- f(x+h) = valor de la función a la derecha del punto
- f(x−h) = valor de la función a la izquierda del punto

---

## Algoritmo

Definir la función que se desea derivar.

Seleccionar el punto x donde se calculará la derivada.

Elegir un valor pequeño para h.

Calcular los puntos x−h y x+h.

Evaluar la función en ambos puntos.

Sustituir los valores obtenidos en la fórmula de diferencia centrada.

Realizar las operaciones correspondientes.

Obtener la aproximación de la derivada.

Comparar con la derivada exacta si se conoce.

---

## Ejemplo

f(x) = x³ + 2x      x = 1      h = 0.5

Puntos utilizados:

x−h = 0.5
x   = 1.0
x+h = 1.5

Evaluaciones:

f(0.5) = 1.1250
f(1.5) = 6.3750

Aplicando la fórmula:

f'(1) ≈ (6.3750 − 1.1250) / (2·0.5)

f'(1) ≈ 5.2500

Derivada exacta:

f'(x) = 3x² + 2

f'(1) = 5.0000

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x³ + 2x, en x = 1, con h = 0.5

| Punto | x     | f(x) |
|--------|-------|--------|
| x−h | 0.5 | 1.1250 |
| x   | 1.0 | 3.0000 |
| x+h | 1.5 | 6.3750 |

f'(1) ≈ (6.3750 − 1.1250) / (2·0.5)

f'(1) ≈ 5.2500

---

**Ejercicio:** f(x) = x² + 3x, en x = 2, con h = 0.5

| Punto | x     | f(x) |
|--------|-------|--------|
| x−h | 1.5 | 6.7500 |
| x   | 2.0 | 10.0000 |
| x+h | 2.5 | 13.7500 |

f'(2) ≈ (13.7500 − 6.7500) / (2·0.5)

f'(2) ≈ 7.0000

**Resultado:**
- Entrada: f(x) = x² + 3x, x = 2, h = 0.5
- Resultado esperado: 7.0000
- Resultado aproximado: 7.0000
- Puntos utilizados: 3
- Error aproximado: 0.0000
