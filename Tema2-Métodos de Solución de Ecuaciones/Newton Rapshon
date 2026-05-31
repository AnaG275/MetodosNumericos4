# Método de Newton-Raphson

def metodo_newton(funcion, derivada, aproximacion_inicial,
                  tol=1e-6, limite_iteraciones=100):

    aproximacion = aproximacion_inicial
    paso = 1

    print(f"{'Paso':<8}{'Valor x':<15}{'f(x)':<15}{'Error':<15}")
    print("=" * 55)

    while paso <= limite_iteraciones:

        valor_funcion = funcion(aproximacion)
        valor_derivada = derivada(aproximacion)

        if abs(valor_derivada) < 1e-12:
            print("\nProceso detenido: derivada muy cercana a cero.")
            return None

        siguiente = aproximacion - (valor_funcion / valor_derivada)

        diferencia = abs(siguiente - aproximacion)

        print(
            f"{paso:<8}"
            f"{siguiente:<15.6f}"
            f"{funcion(siguiente):<15.6f}"
            f"{diferencia:<15.6f}"
        )

        if diferencia <= tol:
            print(f"\nRaíz aproximada: {siguiente:.6f}")
            print(f"Iteraciones utilizadas: {paso}")
            return siguiente

        aproximacion = siguiente
        paso += 1

    print("\nNo se obtuvo convergencia.")
    return None


# Ejemplo
print("=== Ejemplo: f(x) = x² - 5 ===")

def funcion1(x):
    return x**2 - 5

def derivada1(x):
    return 2 * x

metodo_newton(funcion1, derivada1, aproximacion_inicial=2.0)


# Ejercicio
print("\n=== Ejercicio: f(x) = x³ - 8 ===")

def funcion2(x):
    return x**3 - 8

def derivada2(x):
    return 3 * x**2

metodo_newton(funcion2, derivada2, aproximacion_inicial=1.5)
