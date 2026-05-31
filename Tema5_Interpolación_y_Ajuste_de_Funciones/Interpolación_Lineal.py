# Interpolación Lineal

x0, y0 = 1, 2
x1, y1 = 3, 8

x = 1.5

# Pendiente
m = (y1 - y0) / (x1 - x0)

# Interpolación
P = y0 + m * (x - x0)

print(f"m = {m:.4f}")
print(f"P({x}) = {P:.4f}")
