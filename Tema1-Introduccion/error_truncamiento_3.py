# ============================================================
# TEMA: Error de Truncamiento
# EJERCICIO 3: Serie para ln(1+x)
# ============================================================
# ln(1+x) = x - x^2/2 + x^3/3 - x^4/4 + ...  para |x| <= 1

import math

def ln_taylor(x, n_terminos):
    """Aproximación de ln(1+x) usando serie de potencias."""
    suma = 0.0
    for k in range(1, n_terminos + 1):
        suma += ((-1) ** (k + 1)) * (x ** k) / k
    return suma

x = 0.5  # ln(1.5)
valor_real = math.log(1 + x)

print("=" * 60)
print("  ERROR DE TRUNCAMIENTO - Serie para ln(1+x)")
print("=" * 60)
print(f"  x = {x}, calculando ln({1+x})")
print(f"  Valor real = {valor_real:.10f}\n")
print(f"  {'Términos':>8} | {'Aprox':>14} | {'Error Trunc.':>14}")
print("-" * 60)

for n in [1, 2, 3, 5, 10, 20]:
    aprox = ln_taylor(x, n)
    et    = abs(valor_real - aprox)
    print(f"  {n:>8} | {aprox:>14.10f} | {et:>14.10f}")

print("=" * 60)

# Casos de prueba
print("\n  CASOS DE PRUEBA")
tolerancias = {5: 1e-3, 10: 1e-5, 20: 1e-9}
for n, tol in tolerancias.items():
    et = abs(valor_real - ln_taylor(x, n))
    estado = "OK" if et < tol else "REVISAR"
    print(f"  n={n:>2}: ET={et:.2e} < {tol:.0e} [{estado}]")
