# Método de Euler

## Definición
El Método de Euler es una técnica numérica utilizada para aproximar la solución
de ecuaciones diferenciales ordinarias de primer orden con condición inicial.

Se basa en avanzar paso a paso utilizando la pendiente proporcionada por la
ecuación diferencial en cada punto. Es uno de los métodos más sencillos para
resolver problemas de valor inicial, aunque su precisión depende del tamaño del
paso utilizado.

Su error global es proporcional al tamaño del paso h, por lo que se considera
un método de primer orden.

---

## Fórmula

**Ecuación diferencial:**

    y' = f(x,y)

**Fórmula de Euler:**

    y(n+1) = y(n) + h·f(x(n),y(n))

**Actualización de x:**

    x(n+1) = x(n) + h

Donde:
- h → tamaño del paso
- x(n) → valor actual de x
- y(n) → aproximación actual de y
- y(n+1) → siguiente aproximación
- f(x,y) → función de la ecuación diferencial

---

## Algoritmo

Definir la ecuación diferencial y' = f(x,y)

Ingresar la condición inicial:
- x₀
- y₀

Definir el tamaño del paso h

Definir el valor final de x

Calcular la pendiente:

    f(x(n),y(n))

Aplicar la fórmula de Euler:

    y(n+1) = y(n) + h·f(x(n),y(n))

Actualizar:

    x(n+1) = x(n) + h

Repetir hasta alcanzar el valor deseado de x

Mostrar la aproximación obtenida

---

## Ejemplo

Ecuación diferencial:

    y' = x + y

Condición inicial:

    y(0) = 1

Paso:

    h = 0.1

Iteración 1:

    x₀ = 0
    y₀ = 1

    y₁ = 1 + 0.1(0 + 1)
    y₁ = 1.1

Iteración 2:

    x₁ = 0.1
    y₁ = 1.1

    y₂ = 1.1 + 0.1(0.1 + 1.1)
    y₂ = 1.22

Iteración 3:

    x₂ = 0.2
    y₂ = 1.22

    y₃ = 1.22 + 0.1(0.2 + 1.22)
    y₃ = 1.362

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** y' = x + y, y(0)=1, h=0.1, hasta x=0.5

| n | x(n) | y(n) aproximado |
|---|------|-----------------|
| 0 | 0.0  | 1.0000 |
| 1 | 0.1  | 1.1000 |
| 2 | 0.2  | 1.2200 |
| 3 | 0.3  | 1.3620 |
| 4 | 0.4  | 1.5282 |
| 5 | 0.5  | 1.7210 |

**Ejercicio:** y' = y − x² + 1, y(0)=0.5, h=0.2, hasta x=1

| n | x(n) | y(n) aproximado |
|---|------|-----------------|
| 0 | 0.0  | 0.5000 |
| 1 | 0.2  | 0.8000 |
| 2 | 0.4  | 1.1520 |
| 3 | 0.6  | 1.5504 |
| 4 | 0.8  | 1.9885 |
| 5 | 1.0  | 2.4582 |

**Resultado:**
- Entrada: y' = y − x² + 1
- Condición inicial: y(0)=0.5
- Tamaño de paso: h = 0.2
- Valor final: x = 1
- Resultado aproximado: y(1) = 2.4582
- Método utilizado: Euler explícito
