# ============================================================
# TEMA: Error de Truncamiento
# EJERCICIO 1: Serie de Taylor para e^x
# ============================================================
# Aproximar e^x usando los primeros n términos de la serie de Taylor
# e^x = 1 + x + x^2/2! + x^3/3! + ...

import math

def exp_taylor(x, n_terminos):
    """Aproximación de e^x usando n términos de la serie de Taylor."""
    suma = 0.0
    for k in range(n_terminos):
        suma += (x ** k) / math.factorial(k)
    return suma

x = 1.0  # calcular e^1 = e
valor_real = math.exp(x)

print("=" * 60)
print("  ERROR DE TRUNCAMIENTO - Serie de Taylor para e^x")
print("=" * 60)
print(f"  Calculando e^{x}, valor real = {valor_real:.10f}\n")
print(f"  {'Términos':>8} | {'Aprox':>14} | {'Error Trunc.':>14}")
print("-" * 60)

for n in [1, 2, 3, 4, 5, 7, 10]:
    aprox = exp_taylor(x, n)
    et    = abs(valor_real - aprox)
    print(f"  {n:>8} | {aprox:>14.8f} | {et:>14.8f}")

print("=" * 60)

# Casos de prueba
print("\n  CASOS DE PRUEBA")
assert round(exp_taylor(1, 1), 4) == 1.0,     "Fallo n=1"
assert round(exp_taylor(1, 2), 4) == 2.0,     "Fallo n=2"
assert round(exp_taylor(1, 3), 4) == 2.5,     "Fallo n=3"
print("  Casos de prueba correctos.")
