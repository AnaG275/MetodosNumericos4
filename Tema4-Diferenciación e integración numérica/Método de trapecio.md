# Regla del Trapecio

## Definición
La Regla del Trapecio es un método de integración numérica que estima
el valor de una integral definida reemplazando la curva por segmentos
rectos. El área bajo la función se aproxima mediante uno o varios
trapecios, cuyos resultados se suman para obtener una aproximación de
la integral.

Es uno de los métodos más sencillos de implementar y suele utilizarse
como base para técnicas de integración más avanzadas.

---

## Fórmula

Para un solo intervalo:

∫[a,b] f(x) dx ≈ ((b-a)/2) · [f(a) + f(b)]

Para varios subintervalos:

∫[a,b] f(x) dx ≈ (h/2) · [f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]

Donde:

- h = (b − a)/n
- n = número de subintervalos
- xᵢ = a + i·h

---

## Algoritmo

Definir la función que se desea integrar.

Establecer los límites de integración a y b.

Seleccionar el número de subintervalos n.

Calcular el tamaño de paso h.

Generar los puntos x₀, x₁, ..., xₙ.

Evaluar la función en cada punto.

Sumar los valores de los extremos.

Multiplicar por dos las evaluaciones de los puntos intermedios.

Aplicar la fórmula de la Regla del Trapecio.

Obtener la aproximación de la integral.

---

## Ejemplo

f(x) = x² + 1      Intervalo [0,2]

Valores:

f(0) = 1

f(2) = 5

Aplicando la fórmula:

I ≈ ((2−0)/2) · (1 + 5)

I ≈ 6.0000

Valor exacto:

I = 4.6667

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** ∫[0,2] (x² + 1) dx

| Punto | x | f(x) |
|--------|------|--------|
| a | 0.0 | 1.0000 |
| b | 2.0 | 5.0000 |

Cálculo:

I ≈ ((2−0)/2) · (1 + 5)

I ≈ 6.0000

---

**Ejercicio:** ∫[1,3] (x² + 2x) dx

| Punto | x | f(x) |
|--------|------|--------|
| a | 1.0 | 3.0000 |
| b | 3.0 | 15.0000 |

Cálculo:

I ≈ ((3−1)/2) · (3 + 15)

I ≈ 18.0000

Valor exacto:

I = 17.3333

---

**Resultado:**
- Entrada: ∫[1,3] (x² + 2x) dx
- Resultado esperado: 17.3333
- Resultado aproximado: 18.0000
- Subintervalos utilizados: 1
- Error aproximado: 0.6667
