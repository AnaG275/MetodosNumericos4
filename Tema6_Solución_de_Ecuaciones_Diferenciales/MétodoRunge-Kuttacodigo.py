# Método de Runge-Kutta
#### El método de Runge-Kutta es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias. Su objetivo es obtener aproximaciones más precisas que el método de Euler utilizando varios cálculos de pendiente en cada paso.
#### El método más usado es el de Runge-Kutta de cuarto orden (RK4), porque ofrece buena precisión y es fácil de implementar. Este método calcula cuatro pendientes diferentes y luego obtiene un promedio ponderado para encontrar el siguiente valor aproximado de la función.

### Codigo Principal

```python
def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
```

### Codigo 1:
```python
def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

def f(x, y):
    return x + y

runge_kutta(f, 0, 1, 0.1, 5)
```
##### Resultado:
##### x       y
##### 0       1
##### 0.1     1.1103
##### 0.2     1.2428
##### 0.3     1.3997
##### 0.4     1.5836
##### 0.5     1.7974


### Codigo 2:
```python
def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

def f(x, y):
    return x - y

runge_kutta(f, 0, 2, 0.2, 5)
```
##### Resultado:
##### x       y
##### 0       2
##### 0.2     1.6738
##### 0.4     1.4189
##### 0.6     1.2296
##### 0.8     1.1013
##### 1.0     1.0293


### Codigo 3:
```python
def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

def f(x, y):
    return y - x

runge_kutta(f, 1, 1, 0.1, 6)
```
##### Resultado:
##### x       y
##### 1.0     1
##### 1.1     0.9948
##### 1.2     0.9786
##### 1.3     0.9501
##### 1.4     0.908
##### 1.5     0.8508
##### 1.6     0.7771


### Codigo 4:
```python
def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

def f(x, y):
    return x * y

runge_kutta(f, 0, 1, 0.25, 4)
```
##### Resultado:
x       y
###### 


##### 0       1
##### 0.25    1.0317
##### 0.5     1.1331
##### 0.75    1.3248
##### 1.0     1.6486


### Codigo 5:
```python
def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

def f(x, y):
    return x**2 + y

runge_kutta(f, 0, 1, 0.1, 5)
```
##### Resultado:
##### x       y
##### 0       1
##### 0.1     1.1107
##### 0.2     1.2465
##### 0.3     1.4102
##### 0.4     1.6058
##### 0.5     1.8377
