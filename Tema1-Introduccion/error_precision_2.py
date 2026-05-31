# ============================================================
# TEMA: Error de Precisión
# EJERCICIO 2: Cifras significativas en cálculos
# ============================================================

def redondear_sig(x, n):
    """Redondea x a n cifras significativas."""
    from math import log10, floor
    if x == 0:
        return 0
    d = floor(log10(abs(x)))
    factor = 10 ** (n - d - 1)
    return round(x * factor) / factor

valor = 123456.789
print("=" * 55)
print("  ERROR DE PRECISIÓN - Cifras significativas")
print("=" * 55)
print(f"  Valor original: {valor}\n")
print(f"  {'Cifras sig.':>12} | {'Valor redondeado':>18} | {'Error':>12}")
print("-" * 55)

for n in [1, 2, 3, 4, 5, 6]:
    apr = redondear_sig(valor, n)
    er  = abs(valor - apr)
    erp = er / valor * 100
    print(f"  {n:>12} | {apr:>18.6f} | {erp:>10.4f} %")

print("=" * 55)

# Operaciones con pérdida de precisión
a = 1234567890.1
b = 1234567890.2
print(f"\n  a = {a}")
print(f"  b = {b}")
print(f"  b - a = {b - a:.10f}  (esperado: 0.1)")
print(f"  Error = {abs((b - a) - 0.1):.2e}")

# Casos de prueba
print("\n  CASOS DE PRUEBA")
assert redondear_sig(123456.789, 3) == 123000, f"Esperado 123000"
assert redondear_sig(0.004567, 2) == 0.0046, f"Esperado 0.0046"
print("  Casos de prueba correctos.")
