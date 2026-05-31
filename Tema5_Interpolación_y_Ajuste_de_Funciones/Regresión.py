# Regresión Lineal Simple

def regresion_lineal(x, y):
    n = len(x)

    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(xi * yi for xi, yi in zip(x, y))
    suma_x2 = sum(xi**2 for xi in x)

    # Coeficientes de la recta y = a + bx
    b = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x**2)
    a = (suma_y - b * suma_x) / n

    return a, b

# Datos del ejercicio
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Calcular regresión
a, b = regresion_lineal(x, y)

print(f"Ecuación de la recta: y = {a:.4f} + {b:.4f}x")

# Predicción para x = 6
x_pred = 6
y_pred = a + b * x_pred

print(f"Predicción para x = {x_pred}: y = {y_pred:.4f}")
