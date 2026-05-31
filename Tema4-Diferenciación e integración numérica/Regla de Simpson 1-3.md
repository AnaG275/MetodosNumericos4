# Regla de Simpson 1/3

## Definición
La Regla de Simpson 1/3 es un método de integración numérica que aproxima
el área bajo una curva mediante funciones cuadráticas. En lugar de unir los
puntos con segmentos rectos, utiliza parábolas para representar de manera más
precisa el comportamiento de la función dentro de cada intervalo.

Este método suele proporcionar mejores resultados que la Regla del Trapecio
cuando la función es suave y continua. Para aplicarlo correctamente, el número
de subintervalos debe ser par.

---

## Fórmula

∫[a,b] f(x) dx ≈ (h/3) · [f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + 4f(xₙ₋₁) + f(xₙ)]

Donde:

- h = (b − a) / n
- n = número de subintervalos (debe ser par)
- xᵢ = a + i·h

Coeficientes utilizados:

1, 4, 2, 4, 2, ..., 4, 1

---

## Algoritmo

Definir la función que se desea integrar.

Establecer los límites de integración a y b.

Seleccionar un número par de subintervalos n.

Calcular el tamaño de paso h.

Generar los puntos x₀, x₁, ..., xₙ.

Evaluar la función en cada punto.

Multiplicar las evaluaciones por los coeficientes correspondientes.

Sumar todos los términos obtenidos.

Multiplicar el resultado por h/3.

Mostrar la aproximación de la integral.

---

## Ejemplo

f(x) = x³ + 1      Intervalo [0,2]      n = 4

h = (2 − 0)/4 = 0.5

Puntos:

x₀ = 0.0
x₁ = 0.5
x₂ = 1.0
x₃ = 1.5
x₄ = 2.0

Evaluaciones:

f(0.0) = 1.0000
f(0.5) = 1.1250
f(1.0) = 2.0000
f(1.5) = 4.3750
f(2.0) = 9.0000

Aplicando Simpson 1/3:

I ≈ (0.5/3)[1 + 4(1.1250) + 2(2.0000) + 4(4.3750) + 9]

I ≈ 6.0000

Valor exacto:

I = 6.0000

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** ∫[0,2] (x³ + 1) dx, con n = 4

| i | xi   | f(xi) | Coeficiente |
|---|------|--------|-------------|
| 0 | 0.00 | 1.0000 | 1 |
| 1 | 0.50 | 1.1250 | 4 |
| 2 | 1.00 | 2.0000 | 2 |
| 3 | 1.50 | 4.3750 | 4 |
| 4 | 2.00 | 9.0000 | 1 |

**Ejercicio:** ∫[1,3] (x² + 2x) dx, con n = 4

| i | xi   | f(xi) | Coeficiente |
|---|------|--------|-------------|
| 0 | 1.00 | 3.0000 | 1 |
| 1 | 1.50 | 5.2500 | 4 |
| 2 | 2.00 | 8.0000 | 2 |
| 3 | 2.50 | 11.2500| 4 |
| 4 | 3.00 | 15.0000| 1 |

**Resultado:**
- Entrada: ∫[1,3] (x² + 2x) dx
- Resultado esperado: 17.3333
- Resultado aproximado: 17.3333
- Subintervalos utilizados: 4
- Error aproximado: 0.0000
