def simpson_38(a, b, n):
    def f(x):
        return x**2
    
    if n % 3 != 0:
        return "Error: n debe ser múltiplo de 3"
    
    h = (b - a) / n
    
    suma = f(a) + f(b)
    
    for i in range(1, n):
        xi = a + i*h
        
        if i % 3 == 0:
            suma = suma + 2*f(xi)
        else:
            suma = suma + 3*f(xi)
    
    resultado = (3*h/8) * suma
    
    return resultado


print("Ideal:", simpson_38(0, 3, 6))
print("Error:", simpson_38(0, np.pi, 3))
print("Práctico:", simpson_38(0, 1, 6))