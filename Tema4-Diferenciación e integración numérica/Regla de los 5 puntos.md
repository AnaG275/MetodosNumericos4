# Regla de los 5 Puntos

## Definición
La Regla de los 5 Puntos es un método de diferenciación numérica que
permite estimar la derivada de una función utilizando cinco valores
cercanos al punto de interés. Al considerar dos puntos a la izquierda
y dos a la derecha, proporciona una aproximación más precisa que la
Regla de los 3 Puntos.

Este método es especialmente útil cuando se requiere reducir el error
de truncamiento y obtener resultados más cercanos a la derivada exacta.

---

## Fórmula

f'(x) ≈ (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)) / (12h)

Donde:

- f'(x) = derivada aproximada en el punto x
- h = tamaño del incremento
- f(x+2h) = valor de la función dos pasos a la derecha
- f(x+h) = valor de la función un paso a la derecha
- f(x-h) = valor de la función un paso a la izquierda
- f(x-2h) = valor de la función dos pasos a la izquierda

---

## Algoritmo

Definir la función que se desea derivar.

Seleccionar el punto x donde se calculará la derivada.

Elegir un valor adecuado para h.

Calcular los puntos x−2h, x−h, x+h y x+2h.

Evaluar la función en cada uno de esos puntos.

Sustituir los valores en la fórmula de los 5 puntos.

Realizar las operaciones indicadas.

Obtener la aproximación de la derivada.

Comparar con la solución exacta si está disponible.

---

## Ejemplo

f(x) = x³ + x      x = 2      h = 0.5

Puntos utilizados:

x−2h = 1.0
x−h  = 1.5
x+h  = 2.5
x+2h = 3.0

Evaluaciones:

f(1.0) = 2.0000
f(1.5) = 4.8750
f(2.5) = 18.1250
f(3.0) = 30.0000

Aplicando la fórmula:

f'(2) ≈ (-30.0000 + 8(18.1250) - 8(4.8750) + 2.0000) / (12·0.5)

f'(2) ≈ 13.0000

Derivada exacta:

f'(x) = 3x² + 1

f'(2) = 13.0000

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x³ + x, en x = 2, con h = 0.5

| Punto | x | f(x) | Coeficiente |
|--------|------|---------|-------------|
| x−2h | 1.0 | 2.0000 | +1 |
| x−h | 1.5 | 4.8750 | −8 |
| x+h | 2.5 | 18.1250 | +8 |
| x+2h | 3.0 | 30.0000 | −1 |

f'(2) ≈ (-30.0000 + 8(18.1250) - 8(4.8750) + 2.0000) / 6

f'(2) ≈ 13.0000

---

**Ejercicio:** f(x) = x² + 2x, en x = 3, con h = 0.5

| Punto | x | f(x) | Coeficiente |
|--------|------|---------|-------------|
| x−2h | 2.0 | 8.0000 | +1 |
| x−h | 2.5 | 11.2500 | −8 |
| x+h | 3.5 | 19.2500 | +8 |
| x+2h | 4.0 | 24.0000 | −1 |

f'(3) ≈ (-24.0000 + 8(19.2500) - 8(11.2500) + 8.0000) / 6

f'(3) ≈ 8.0000

**Resultado:**
- Entrada: f(x) = x² + 2x, x = 3, h = 0.5
- Resultado esperado: 8.0000
- Resultado aproximado: 8.0000
- Puntos utilizados: 5
- Error aproximado: 0.0000
