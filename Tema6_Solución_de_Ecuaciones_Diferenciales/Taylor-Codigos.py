### Codigo principal:
``` python
# Método de Taylor de segundo orden

def taylor(f, df, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        y = y + h * f(x, y) + (h**2 / 2) * df(x, y)
        x = x + h
```


### Codigo 1:
``` python
def taylor(f, df, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        y = y + h * f(x, y) + (h**2 / 2) * df(x, y)
        x = x + h

def f(x, y):
    return x + y

def df(x, y):
    return 1 + x + y

taylor(f, df, 0, 1, 0.1, 5)
```
#### Resultado:
##### x       y
##### 0       1
##### 0.1     1.11
##### 0.2     1.2421
##### 0.3     1.3985
##### 0.4     1.5818
##### 0.5     1.7949



### Codigo 2:
``` python
def taylor(f, df, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        y = y + h * f(x, y) + (h**2 / 2) * df(x, y)
        x = x + h

def f(x, y):
    return x - y

def df(x, y):
    return 1 - x + y

taylor(f, df, 0, 2, 0.2, 5)
```
#### Resultado:
##### x       y
##### 0       2
##### 0.2     1.68
##### 0.4     1.4304
##### 0.6     1.2468
##### 0.8     1.1253
##### 1.0     1.0625

### Codigo 3:
``` python
def taylor(f, df, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        y = y + h * f(x, y) + (h**2 / 2) * df(x, y)
        x = x + h

def f(x, y):
    return y - x

def df(x, y):
    return y - x - 1

taylor(f, df, 1, 1, 0.1, 6)
```
#### Resultado:
##### x       y
##### 1.0     1
##### 1.1     0.995
##### 1.2     0.9795
##### 1.3     0.9529
##### 1.4     0.9137
##### 1.5     0.8602
##### 1.6     0.7901


### Codigo 4:
``` python
def taylor(f, df, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        y = y + h * f(x, y) + (h**2 / 2) * df(x, y)
        x = x + h

def f(x, y):
    return x * y

def df(x, y):
    return y + x**2 * y

taylor(f, df, 0, 1, 0.25, 4)
```
#### Resultado:
##### x       y
##### 0       1
##### 0.25    1.0312
##### 0.5     1.132
##### 0.75    1.3221
##### 1.0     1.643



### Codigo 5:
``` python
def taylor(f, df, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x,4), "\t", round(y,4))

        y = y + h * f(x, y) + (h**2 / 2) * df(x, y)
        x = x + h

def f(x, y):
    return x**2 + y

def df(x, y):
    return 2*x + x**2 + y

taylor(f, df, 0, 1, 0.1, 5)
```
#### Resultado:
##### x       y
##### 0       1
##### 0.1     1.105
##### 0.2     1.2336
##### 0.3     1.3896
##### 0.4     1.5775
##### 0.5     1.8027
