# ============================================================
# TEMA: Error Absoluto
# EJERCICIO 2: Aproximación del número Pi
# ============================================================
import math

valor_real = math.pi
aproximaciones = [3.14, 3.141, 3.1416]

print("=" * 45)
print("  ERROR ABSOLUTO - Aproximaciones de Pi")
print("=" * 45)
print(f"  Valor real de Pi: {valor_real:.10f}\n")

for aprox in aproximaciones:
    ea = abs(valor_real - aprox)
    print(f"  Aprox = {aprox}")
    print(f"  Error absoluto = {ea:.10f}")
    print("-" * 45)

# Casos de prueba
print("\n  CASOS DE PRUEBA")
casos = [(3.14, 0.0016), (3.141, 0.0006), (3.1416, 0.00001)]
for aprox, esperado in casos:
    ea = abs(valor_real - aprox)
    estado = "OK" if round(ea, 5) <= round(esperado, 5) + 0.00001 else "REVISAR"
    print(f"  Pi ≈ {aprox} -> EA = {ea:.6f}  [{estado}]")
