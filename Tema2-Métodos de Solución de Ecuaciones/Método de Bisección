# Método de Bisección

def metodo_biseccion(funcion, limite_inferior, limite_superior,
                     tol=1e-6, iteraciones_max=100):

    if funcion(limite_inferior) * funcion(limite_superior) > 0:
        print("El intervalo seleccionado no contiene una raíz.")
        return None

    print(f"{'Paso':<8}{'Inferior':<12}{'Superior':<12}"
          f"{'Medio':<12}{'f(medio)':<15}{'Error':<12}")
    print("=" * 75)

    contador = 1

    while contador <= iteraciones_max:

        punto_medio = (limite_inferior + limite_superior) / 2
        valor_medio = funcion(punto_medio)

        margen_error = abs(limite_superior - limite_inferior) / 2

        print(
            f"{contador:<8}"
            f"{limite_inferior:<12.6f}"
            f"{limite_superior:<12.6f}"
            f"{punto_medio:<12.6f}"
            f"{valor_medio:<15.6f}"
            f"{margen_error:<12.6f}"
        )

        if abs(valor_medio) <= tol or margen_error <= tol:
            print(f"\nRaíz aproximada: {punto_medio:.6f}")
            print(f"Iteraciones realizadas: {contador}")
            return punto_medio

        if funcion(limite_inferior) * valor_medio < 0:
            limite_superior = punto_medio
        else:
            limite_inferior = punto_medio

        contador += 1

    print("\nNo se alcanzó la convergencia.")
    return None


# Ejemplo
print("=== Ejemplo: f(x) = x³ - 4 ===")

def funcion1(x):
    return x**3 - 4

metodo_biseccion(funcion1, 1.0, 2.0)


# Ejercicio
print("\n=== Ejercicio: f(x) = x² - 5 ===")

def funcion2(x):
    return x**2 - 5

metodo_biseccion(funcion2, 2.0, 3.0)
