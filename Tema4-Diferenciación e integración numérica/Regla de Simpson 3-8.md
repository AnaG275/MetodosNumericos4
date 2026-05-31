# Regla de Simpson 3/8

## Definición
La Regla de Simpson 3/8 es un método de integración numérica que aproxima
el valor de una integral definida utilizando polinomios de tercer grado.
A diferencia de la Regla de Simpson 1/3, trabaja con grupos de tres
subintervalos y requiere que el número de subintervalos sea múltiplo de 3.

Este método proporciona una aproximación muy precisa para funciones suaves
y puede integrar exactamente polinomios de hasta grado 3.

---

## Fórmula

∫[a,b] f(x) dx ≈ (3h/8) * [f(x₀) + 3f(x₁) + 3f(x₂) + 2f(x₃) + ... + 3f(xₙ₋₂) + 3f(xₙ₋₁) + f(xₙ)]

Donde:
- h = (b - a) / n
- n = número de subintervalos (debe ser múltiplo de 3)
- xᵢ = a + i·h
- Patrón de coeficientes:
  1, 3, 3, 2, 3, 3, 2, ..., 3, 3, 1

---

## Algoritmo

Definir la función f(x)

Definir el límite inferior a

Definir el límite superior b

Definir el número de subintervalos n

Verificar que n sea múltiplo de 3

Calcular el tamaño del paso:

h = (b - a) / n

Generar los puntos x₀, x₁, ..., xₙ

Evaluar la función en cada punto

Aplicar los coeficientes correspondientes según la posición

Sumar todos los términos obtenidos

Multiplicar la suma por (3h/8)

Obtener la aproximación de la integral

---

## Ejemplo

Integral:

∫[0,3] (x³ + 1) dx

Con n = 3

| Punto | x | f(x) |
|--------|------|--------|
| x₀ | 0.0 | 1.0000 |
| x₁ | 1.0 | 2.0000 |
| x₂ | 2.0 | 9.0000 |
| x₃ | 3.0 | 28.0000 |

Aplicando la fórmula:

I = (3·1/8)[1 + 3(2) + 3(9) + 28]

I = (3/8)(62)

I = 23.2500

Valor exacto = 23.2500

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** ∫[0,3] (x³ + 1) dx, n = 3

| i | xᵢ | f(xᵢ) | Coeficiente |
|---|------|--------|-------------|
| 0 | 0.0000 | 1.0000 | 1 |
| 1 | 1.0000 | 2.0000 | 3 |
| 2 | 2.0000 | 9.0000 | 3 |
| 3 | 3.0000 | 28.0000 | 1 |

**Resultado:** `Simpson 3/8 ≈ 23.2500`

---

**Ejercicio:** ∫[0,3] (x² + 2x) dx, n = 3

| i | xᵢ | f(xᵢ) | Coeficiente |
|---|------|--------|-------------|
| 0 | 0.0000 | 0.0000 | 1 |
| 1 | 1.0000 | 3.0000 | 3 |
| 2 | 2.0000 | 8.0000 | 3 |
| 3 | 3.0000 | 15.0000 | 1 |

**Resultado:**
- Entrada: f(x) = x² + 2x, a = 0, b = 3, n = 3
- Resultado esperado: 18.0000
- Resultado float:    18.0000
- Subintervalos:      3
- Error acumulado:    0.0000
