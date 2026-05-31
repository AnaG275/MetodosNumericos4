# Interpolación Cuadrática

## Definición
La Interpolación Cuadrática es un método numérico que permite estimar el
valor de una función utilizando un polinomio de segundo grado que pasa
exactamente por tres puntos conocidos.

Este método proporciona una aproximación más precisa que la interpolación
lineal cuando los datos presentan curvatura, ya que utiliza una parábola
para representar el comportamiento de la función entre los puntos dados.

---

## Fórmula

Polinomio de Lagrange de segundo grado:

P(x) = y₀L₀(x) + y₁L₁(x) + y₂L₂(x)

Donde:

L₀(x) = ((x - x₁)(x - x₂)) / ((x₀ - x₁)(x₀ - x₂))

L₁(x) = ((x - x₀)(x - x₂)) / ((x₁ - x₀)(x₁ - x₂))

L₂(x) = ((x - x₀)(x - x₁)) / ((x₂ - x₀)(x₂ - x₁))

Donde:
- (x₀,y₀), (x₁,y₁), (x₂,y₂) → puntos conocidos
- P(x) → valor interpolado
- L₀, L₁ y L₂ → polinomios base de Lagrange

---

## Algoritmo

Definir tres puntos conocidos

Seleccionar el valor x donde se desea interpolar

Calcular los polinomios base L₀(x), L₁(x) y L₂(x)

Multiplicar cada polinomio por su valor y correspondiente

Sumar los términos obtenidos

Construir el polinomio cuadrático

Evaluar el polinomio en el valor deseado

Obtener la aproximación buscada

---

## Ejemplo

Puntos:

(1,1), (2,4), (3,9)

Interpolar en:

x = 2.5

Tabla de datos:

| Punto | x | y |
|--------|----|----|
| P₀ | 1 | 1 |
| P₁ | 2 | 4 |
| P₂ | 3 | 9 |

Aplicando la fórmula de Lagrange:

P(2.5) = 6.25

Valor exacto:

f(2.5) = (2.5)² = 6.25

---

## Ejemplo y Caso de Prueba

**Caso de prueba:**

Puntos:

(0,1), (1,3), (2,7)

Interpolar en x = 1.5

| Punto | x | y |
|--------|----|----|
| P₀ | 0 | 1 |
| P₁ | 1 | 3 |
| P₂ | 2 | 7 |

**Resultado:** `P(1.5) = 4.75`

---

**Ejercicio:**

Puntos:

(1,2), (2,5), (4,17)

Interpolar en x = 3

| Punto | x | y |
|--------|----|----|
| P₀ | 1 | 2 |
| P₁ | 2 | 5 |
| P₂ | 4 | 17 |

**Resultado:**
- Entrada: (1,2), (2,5), (4,17), x = 3
- Resultado esperado: 10.0000
- Resultado float:    10.0000
- Polinomio utilizado: Cuadrático de Lagrange
- Error acumulado:    0.0000
