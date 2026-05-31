import numpy as np

def gauss(a, b):
    # 1. función
    def f(x):
        return x**2
    
    # 2. punto medio
    xm = (a + b) / 2
    
    # 3. radio
    xr = (b - a) / 2
    
    # 4. puntos
    x1 = -1/np.sqrt(3)
    x2 = 1/np.sqrt(3)
    
    # 5. suma
    suma = f(xm + xr*x1) + f(xm + xr*x2)
    
    # 6. resultado
    resultado = xr * suma
    
    return resultado


print("Ideal:", gauss(0, 2))
print("Error:", gauss(0, np.pi))
print("Práctico:", gauss(0, 1))