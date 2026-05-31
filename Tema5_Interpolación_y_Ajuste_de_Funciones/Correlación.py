import math

# Datos del ejemplo
x = [2, 4, 6, 8, 10]
y = [50, 60, 70, 85, 95]

n = len(x)

# Medias
x_media = sum(x) / n
y_media = sum(y) / n

# Sumas necesarias
suma_xy = 0
suma_x2 = 0
suma_y2 = 0

for i in range(n):
    dx = x[i] - x_media
    dy = y[i] - y_media

    suma_xy += dx * dy
    suma_x2 += dx ** 2
    suma_y2 += dy ** 2

# Correlación de Pearson
r = suma_xy / (math.sqrt(suma_x2) * math.sqrt(suma_y2))

print("x̄ =", round(x_media, 4))
print("ȳ =", round(y_media, 4))
print("Σ(xi-x̄)(yi-ȳ) =", round(suma_xy, 4))
print("Σ(xi-x̄)² =", round(suma_x2, 4))
print("Σ(yi-ȳ)² =", round(suma_y2, 4))
print("r =", round(r, 4))
