# ============================================================
# TEMA: Error Relativo
# EJERCICIO 3: Cálculo del número de Euler (e)
# ============================================================
import math

valor_real = math.e  # 2.718281828...

aproximaciones = [2.7, 2.71, 2.718, 2.7183]

print("=" * 55)
print("  ERROR RELATIVO - Aproximaciones del número e")
print("=" * 55)
print(f"  Valor real de e: {valor_real:.10f}\n")

for aprox in aproximaciones:
    ea  = abs(valor_real - aprox)
    er  = ea / valor_real
    erp = er * 100
    print(f"  e ≈ {aprox}")
    print(f"    Error absoluto     = {ea:.8f}")
    print(f"    Error relativo (%) = {erp:.6f} %")
    print("-" * 55)

# Casos de prueba
print("\n  CASOS DE PRUEBA (verificación decreciente)")
errores = [abs(valor_real - a) / valor_real * 100 for a in aproximaciones]
for i in range(len(errores) - 1):
    assert errores[i] > errores[i+1], f"Error no decrece en paso {i}"
print("  Los errores decrecen correctamente con mayor precisión. OK")
