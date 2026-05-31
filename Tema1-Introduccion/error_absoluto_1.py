# ============================================================
# TEMA: Error Absoluto
# EJERCICIO 1: Aproximación de raíz cuadrada
# ============================================================
# Valor real vs valor aproximado de sqrt(2)
import math

valor_real = math.sqrt(2)
valor_aprox = 1.414

error_absoluto = abs(valor_real - valor_aprox)

print("=" * 45)
print("  ERROR ABSOLUTO - Raíz cuadrada de 2")
print("=" * 45)
print(f"  Valor real    : {valor_real:.10f}")
print(f"  Valor aprox.  : {valor_aprox:.10f}")
print(f"  Error absoluto: {error_absoluto:.10f}")
print("=" * 45)

# Casos de prueba
casos = [
    (math.sqrt(2), 1.414,    "sqrt(2) ≈ 1.414"),
    (math.sqrt(2), 1.4142,   "sqrt(2) ≈ 1.4142"),
    (math.sqrt(2), 1.41421,  "sqrt(2) ≈ 1.41421"),
]

print("\n  CASOS DE PRUEBA")
print("-" * 45)
for real, aprox, desc in casos:
    ea = abs(real - aprox)
    print(f"  {desc}")
    print(f"    Error absoluto = {ea:.10f}\n")
