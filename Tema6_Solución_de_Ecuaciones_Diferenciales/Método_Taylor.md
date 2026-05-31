# Método de Taylor

## Definición
El Método de Taylor es una técnica numérica utilizada para resolver ecuaciones
diferenciales ordinarias mediante el desarrollo en serie de Taylor de la función
solución alrededor de un punto conocido.

Este método utiliza no solo la primera derivada de la función, sino también
derivadas de orden superior, lo que permite obtener aproximaciones más precisas
que métodos simples como Euler cuando dichas derivadas están disponibles.

La precisión del método aumenta conforme se incluyen más términos de la serie
de Taylor.

---

## Fórmula

**Serie de Taylor de segundo orden:**

    y(x+h) ≈ y(x) + h·y'(x) + (h²/2)·y''(x)

**Serie de Taylor de tercer orden:**

    y(x+h) ≈ y(x) + h·y'(x)
                  + (h²/2)·y''(x)
                  + (h³/6)·y'''(x)

Donde:
- h → tamaño del paso
- y'(x) → primera derivada
- y''(x) → segunda derivada
- y'''(x) → tercera derivada
- y(x+h) → aproximación siguiente

---

## Algoritmo

Definir la ecuación diferencial

Determinar las derivadas necesarias:
- y'
- y''
- y'''
- ...

Ingresar la condición inicial:
- x₀
- y₀

Definir el tamaño del paso h

Evaluar las derivadas en el punto actual

Sustituir los valores en la serie de Taylor

Calcular la nueva aproximación y(x+h)

Actualizar el valor de x

Repetir hasta alcanzar el valor deseado

Mostrar la solución aproximada

---

## Ejemplo

Ecuación diferencial:

    y' = y

Condición inicial:

    y(0) = 1

Sabemos que:

    y'' = y

Serie de Taylor de segundo orden:

    y(x+h) = y + h·y + (h²/2)y

Con:

    h = 0.1

Iteración 1:

    y1 = 1 + 0.1(1) + (0.1²/2)(1)

    y1 = 1 + 0.1 + 0.005

    y1 = 1.1050

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** y' = y, y(0)=1, h=0.1, hasta x=0.5

| n | x(n) | y(n) aproximado |
|---|------|-----------------|
| 0 | 0.0  | 1.0000 |
| 1 | 0.1  | 1.1050 |
| 2 | 0.2  | 1.2210 |
| 3 | 0.3  | 1.3492 |
| 4 | 0.4  | 1.4908 |
| 5 | 0.5  | 1.6473 |

Valor exacto:

    y(0.5) = e^0.5 = 1.6487

Error:

    |1.6487 - 1.6473| = 0.0014

**Ejercicio:** y' = x + y, y(0)=1, h=0.2

Derivadas:

    y'  = x + y

    y'' = 1 + y'

    y'' = 1 + x + y

| n | x(n) | y(n) aproximado |
|---|------|-----------------|
| 0 | 0.0  | 1.0000 |
| 1 | 0.2  | 1.2600 |
| 2 | 0.4  | 1.5964 |
| 3 | 0.6  | 2.0231 |
| 4 | 0.8  | 2.5565 |
| 5 | 1.0  | 3.2154 |

**Resultado:**
- Entrada: y' = x + y
- Condición inicial: y(0)=1
- Tamaño de paso: h = 0.2
- Orden utilizado: Taylor de segundo orden
- Resultado aproximado: y(1) = 3.2154
- Precisión: mayor que Euler al incluir derivadas de orden superior
