# ============================================================
# TEMA: Error de Redondeo
# EJERCICIO 1: Suma de números de punto flotante
# ============================================================
# Demostrar cómo el redondeo acumulado afecta sumas

def suma_acumulada(n):
    """Suma 1/n exactamente n veces."""
    total = 0.0
    paso  = 1.0 / n
    for _ in range(n):
        total += paso
    return total

valor_real = 1.0  # La suma debería dar exactamente 1

print("=" * 55)
print("  ERROR DE REDONDEO - Suma de 1/n exactamente n veces")
print("=" * 55)
print(f"  Se espera siempre: {valor_real}\n")
print(f"  {'n':>10} | {'Resultado':>18} | {'Error':>16}")
print("-" * 55)

for n in [10, 100, 1000, 10000, 100000]:
    resultado = suma_acumulada(n)
    error     = abs(valor_real - resultado)
    print(f"  {n:>10} | {resultado:>18.15f} | {error:>16.2e}")

print("=" * 55)

# Casos de prueba
print("\n  CASOS DE PRUEBA")
for n in [10, 100, 1000]:
    r  = suma_acumulada(n)
    er = abs(1.0 - r)
    print(f"  n={n}: resultado={r:.15f}, error={er:.2e}")
