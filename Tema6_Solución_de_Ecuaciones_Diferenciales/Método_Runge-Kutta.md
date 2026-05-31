# Método de Runge-Kutta de Cuarto Orden (RK4)

## Definición
El Método de Runge-Kutta de Cuarto Orden es una técnica numérica utilizada para
resolver ecuaciones diferenciales ordinarias con condiciones iniciales.

A diferencia del Método de Euler, este método calcula varias pendientes dentro
de cada intervalo y las combina para obtener una aproximación mucho más precisa.
Es uno de los métodos más utilizados en ingeniería, física y ciencias debido a
su excelente equilibrio entre precisión y costo computacional.

Su error global es del orden de h⁴, por lo que ofrece resultados muy precisos
incluso con tamaños de paso relativamente grandes.

---

## Fórmula

**Ecuación diferencial:**

    y' = f(x,y)

**Coeficientes de Runge-Kutta:**

    k1 = h·f(xn, yn)

    k2 = h·f(xn + h/2, yn + k1/2)

    k3 = h·f(xn + h/2, yn + k2/2)

    k4 = h·f(xn + h, yn + k3)

**Actualización:**

    yn+1 = yn + (k1 + 2k2 + 2k3 + k4)/6

    xn+1 = xn + h

Donde:
- h → tamaño del paso
- xn → valor actual de x
- yn → aproximación actual de y
- k1, k2, k3, k4 → pendientes intermedias
- f(x,y) → ecuación diferencial

---

## Algoritmo

Definir la ecuación diferencial y' = f(x,y)

Ingresar la condición inicial:
- x₀
- y₀

Definir el tamaño del paso h

Calcular k1

Calcular k2 utilizando k1

Calcular k3 utilizando k2

Calcular k4 utilizando k3

Calcular el nuevo valor:

    yn+1 = yn + (k1 + 2k2 + 2k3 + k4)/6

Actualizar:

    xn+1 = xn + h

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

    k1 = 0.1(0 + 1) = 0.1000

    k2 = 0.1(0.05 + 1.05) = 0.1100

    k3 = 0.1(0.05 + 1.055) = 0.1105

    k4 = 0.1(0.1 + 1.1105) = 0.1211

    y1 = 1 + (0.1000 + 2(0.1100) + 2(0.1105) + 0.1211)/6

    y1 = 1.1103

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** y' = x + y, y(0)=1, h=0.1, hasta x=0.5

| n | x(n) | y(n) aproximado |
|---|------|-----------------|
| 0 | 0.0  | 1.0000 |
| 1 | 0.1  | 1.1103 |
| 2 | 0.2  | 1.2428 |
| 3 | 0.3  | 1.3997 |
| 4 | 0.4  | 1.5836 |
| 5 | 0.5  | 1.7974 |

**Ejercicio:** y' = y − x² + 1, y(0)=0.5, h=0.2, hasta x=1

| n | x(n) | y(n) aproximado |
|---|------|-----------------|
| 0 | 0.0  | 0.5000 |
| 1 | 0.2  | 0.8293 |
| 2 | 0.4  | 1.2141 |
| 3 | 0.6  | 1.6489 |
| 4 | 0.8  | 2.1272 |
| 5 | 1.0  | 2.6408 |

**Resultado:**
- Entrada: y' = y − x² + 1
- Condición inicial: y(0)=0.5
- Tamaño de paso: h = 0.2
- Valor final: x = 1
- Resultado aproximado: y(1) = 2.6408
- Método utilizado: Runge-Kutta de Cuarto Orden (RK4)
- Precisión: superior al Método de Euler para el mismo tamaño de paso
