# Interpolación Cuadrática de Lagrange

x0, y0 = 1, 1
x1, y1 = 2, 8
x2, y2 = 3, 27

x = 1.5

# Bases de Lagrange
L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))

# Interpolación
P = y0 * L0 + y1 * L1 + y2 * L2

print(f"L0 = {L0:.4f}")
print(f"L1 = {L1:.4f}")
print(f"L2 = {L2:.4f}")
print(f"P({x}) = {P:.4f}")
