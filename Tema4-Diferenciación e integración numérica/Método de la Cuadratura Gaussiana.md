# Cuadratura Gaussiana

## Definición
La Cuadratura Gaussiana es un método numérico utilizado para aproximar
integrales definidas mediante una combinación de nodos y pesos previamente
calculados. A diferencia de otras técnicas de integración, selecciona puntos
estratégicos dentro del intervalo para obtener una mayor precisión con un menor
número de evaluaciones de la función.

Es especialmente útil cuando la función es complicada o cuando se busca una
aproximación rápida con un error reducido.

---

## Fórmula

Para una cuadratura de Gauss-Legendre de 2 puntos:

        1
∫[-1,1] f(x) dx ≈ f(- ── ) + f( ── )
       √3         √3

Para un intervalo cualquiera [a,b]:

∫[a,b] f(x) dx ≈ ((b-a)/2) · [f(x₁) + f(x₂)]

Donde:

- x₁ = ((b-a)/2)(-1/√3) + (a+b)/2
- x₂ = ((b-a)/2)( 1/√3) + (a+b)/2

---

## Algoritmo

Definir la función que se desea integrar.

Establecer los límites de integración a y b.

Seleccionar los nodos y pesos de Gauss para el número de puntos elegido.

Transformar los nodos al intervalo [a,b].

Evaluar la función en cada nodo transformado.

Multiplicar cada evaluación por su peso correspondiente.

Sumar los resultados obtenidos.

Multiplicar la suma por el factor (b-a)/2.

Mostrar el valor aproximado de la integral.

---

## Ejemplo

f(x) = x² + 1      Intervalo [0,2]

Nodos transformados:

x₁ = 0.4226
x₂ = 1.5774

Evaluaciones:

f(0.4226) = 1.1786
f(1.5774) = 3.4880

Aplicando la fórmula:

I ≈ ((2-0)/2) · (1.1786 + 3.4880)

I ≈ 4.6666

Valor exacto:

I = 4.6667

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** ∫[0,2] (x² + 1) dx, con 2 puntos de Gauss

| Nodo | t       | x transformado | f(x)   | Peso |
|:----:|:-------:|:--------------:|:------:|:----:|
| 1    | -0.5774 | 0.4226         | 1.1786 | 1    |
| 2    |  0.5774 | 1.5774         | 3.4880 | 1    |

**Ejercicio:** ∫[1,3] (x³ − x + 2) dx, con 2 puntos de Gauss

| Nodo | t       | x transformado | f(x)    | Peso |
|:----:|:-------:|:--------------:|:-------:|:----:|
| 1    | -0.5774 | 1.4226         | 3.4567  | 1    |
| 2    |  0.5774 | 2.5774         | 16.5405 | 1    |

**Resultado:**
- Entrada: ∫[1,3] (x³ − x + 2) dx
- Resultado esperado: 20.0000
- Resultado aproximado: 19.9972
- Nodos utilizados: 2
- Error aproximado: 2.8e-3
