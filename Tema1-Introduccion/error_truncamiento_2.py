# ============================================================
# TEMA: Error de Truncamiento
# EJERCICIO 2: Serie de Maclaurin para sen(x)
# ============================================================
# sen(x) = x - x^3/3! + x^5/5! - x^7/7! + ...

import math

def sin_taylor(x, n_terminos):
    """Aproximación de sen(x) usando serie de Maclaurin."""
    suma = 0.0
    for k in range(n_terminos):
        coef = (-1) ** k
        term = coef * (x ** (2*k + 1)) / math.factorial(2*k + 1)
        suma += term
    return suma

x = math.pi / 6   # sen(30°) = 0.5
valor_real = math.sin(x)

print("=" * 60)
print("  ERROR DE TRUNCAMIENTO - Serie de Maclaurin sen(x)")
print("=" * 60)
print(f"  x = pi/6 = {x:.6f} rad")
print(f"  sen(x) real = {valor_real:.10f}\n")
print(f"  {'Términos':>8} | {'Aprox':>14} | {'Error Trunc.':>14}")
print("-" * 60)

for n in [1, 2, 3, 4, 5]:
    aprox = sin_taylor(x, n)
    et    = abs(valor_real - aprox)
    print(f"  {n:>8} | {aprox:>14.10f} | {et:>14.10f}")

print("=" * 60)

# Casos de prueba
print("\n  CASOS DE PRUEBA")
for n in [1, 2, 3, 4, 5]:
    aprox = sin_taylor(x, n)
    et    = abs(valor_real - aprox)
    prev  = abs(valor_real - sin_taylor(x, n - 1)) if n > 1 else float('inf')
    estado = "MEJORA" if et < prev else "NO MEJORA"
    print(f"  n={n}: ET={et:.2e} [{estado}]")
