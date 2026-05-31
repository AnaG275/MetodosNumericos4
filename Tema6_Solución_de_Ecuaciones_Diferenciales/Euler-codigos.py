
### Codigo principal
 ``` python
def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x, 4), "\t", round(y, 4))

        y = y + h * f(x, y)
        x = x + h
  ```
 ### Codigo 1:
   ``` python
def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x, 4), "\t", round(y, 4))

        y = y + h * f(x, y)
        x = x + h

def f(x, y):
    return x + y

euler(f, 0, 1, 0.1, 5)
  ```
 #### Resultado: 
##### x       y
##### 0       1
##### 0.1     1.1
##### 0.2     1.22
##### 0.3     1.362
##### 0.4     1.5282
##### 0.5     1.721


 ### Codigo 2:
   ``` python
def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x, 4), "\t", round(y, 4))

        y = y + h * f(x, y)
        x = x + h

def f(x, y):
    return x - y

euler(f, 0, 2, 0.2, 5)
   ``` 
 #### Resultado: 
##### x       y
##### 0       2
##### 0.2     1.6
##### 0.4     1.32
##### 0.6     1.136
##### 0.8     1.0288
##### 1.0     0.983



 ### Codigo 3:
   ``` python
def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x, 4), "\t", round(y, 4))

        y = y + h * f(x, y)
        x = x + h

def f(x, y):
    return y - x

euler(f, 1, 1, 0.1, 6)
  ```
 #### Resultado: 
##### x       y
##### 1.0     1
##### 1.1     1
##### 1.2     0.99
##### 1.3     0.969
##### 1.4     0.9359
##### 1.5     0.8895
##### 1.6     0.8284


 ### Codigo 4:
   ``` python
def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x, 4), "\t", round(y, 4))

        y = y + h * f(x, y)
        x = x + h

def f(x, y):
    return x * y

euler(f, 0, 1, 0.25, 4)
  ```
 #### Resultado: 
##### x       y
##### 0       1
##### 0.25    1
##### 0.5     1.0625
##### 0.75    1.1953
##### 1.0     1.4194


 ### Codigo 5:
   ``` python
def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    print("x\t y")

    for i in range(n + 1):
        print(round(x, 4), "\t", round(y, 4))

        y = y + h * f(x, y)
        x = x + h

def f(x, y):
    return x**2 + y

euler(f, 0, 1, 0.1, 5)
  ```
 #### Resultado: 
##### x       y
##### 0       1
##### 0.1     1.1
##### 0.2     1.211
##### .3     1.3361
##### 0.4     1.4797
##### 0.5     1.6477
