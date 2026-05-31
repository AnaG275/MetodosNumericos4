# Interpolación Segmentada (Lineal por Tramos)

def interpolacion_segmentada(x_datos, y_datos, x):
    n = len(x_datos)

    # Verificar que x esté dentro del intervalo
    if x < x_datos[0] or x > x_datos[-1]:
        raise ValueError("El valor de x está fuera del rango de los datos.")

    # Buscar el segmento correspondiente
    for i in range(n - 1):
        if x_datos[i] <= x <= x_datos[i + 1]:
            x0, x1 = x_datos[i], x_datos[i + 1]
            y0, y1 = y_datos[i], y_datos[i + 1]

            # Fórmula de interpolación lineal
            y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)
            return y

# Datos del ejercicio
x_datos = [0, 2, 4, 6, 8]
y_datos = [5, 9, 15, 23, 33]

# Punto a interpolar
x = 5

resultado = interpolacion_segmentada(x_datos, y_datos, x)

print(f"Valor interpolado en x = {x}: {resultado}")
