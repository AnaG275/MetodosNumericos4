# ============================================================
# TEMA: Error de Redondeo
# EJERCICIO 2: Resta de números casi iguales (cancelación catastrófica)
# ============================================================
import math

def raices_estandar(a, b, c):
    """Fórmula cuadrática estándar."""
    disc = b**2 - 4*a*c
    x1 = (-b + math.sqrt(disc)) / (2*a)
    x2 = (-b - math.sqrt(disc)) / (2*a)
    return x1, x2

def raices_estables(a, b, c):
    """Fórmula numéricamente estable (evita cancelación)."""
    disc = b**2 - 4*a*c
    if b >= 0:
        x1 = (-b - math.sqrt(disc)) / (2*a)
    else:
        x1 = (-b + math.sqrt(disc)) / (2*a)
    x2 = c / (a * x1)  # Relación de Vieta
    return x1, x2

a, b, c = 1, -10000, 1

print("=" * 60)
print("  ERROR DE REDONDEO - Cancelación catastrófica")
print("=" * 60)
print(f"  Ecuación: {a}x^2 + ({b})x + {c} = 0\n")

x1e, x2e = raices_estandar(a, b, c)
x1s, x2s = raices_estables(a, b, c)

print(f"  Fórmula estándar   : x1={x1e:.8f}, x2={x2e:.8f}")
print(f"  Fórmula estable    : x1={x1s:.8f}, x2={x2s:.8f}")
x1r = (b - math.sqrt(b**2 - 4*a*c))/(2*a)  # raíz "real"
print(f"\n  Nota: la raíz pequeña con estándar pierde precisión.")
print("=" * 60)

# Casos de prueba
print("\n  CASOS DE PRUEBA")
assert abs(x1s * x2s - c/a) < 1e-6, "Producto de raíces incorrecto"
assert abs(x1s + x2s - (-b/a)) < 1e-6, "Suma de raíces incorrecta"
print("  Relaciones de Vieta verificadas. OK")
