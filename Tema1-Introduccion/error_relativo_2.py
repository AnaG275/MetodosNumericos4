# ============================================================
# TEMA: Error Relativo
# EJERCICIO 2: Masa de un objeto en laboratorio
# ============================================================
import math

def error_relativo(real, aprox):
    return abs(real - aprox) / abs(real)

masa_real = 5.000    # kg (valor de referencia)
mediciones = [4.985, 5.010, 4.997]

print("=" * 50)
print("  ERROR RELATIVO - Masa de un objeto")
print("=" * 50)
print(f"  Masa real de referencia: {masa_real} kg\n")

for m in mediciones:
    ea  = abs(masa_real - m)
    er  = error_relativo(masa_real, m)
    erp = er * 100
    print(f"  Medición : {m} kg")
    print(f"    Error absoluto     = {ea:.4f} kg")
    print(f"    Error relativo     = {er:.6f}")
    print(f"    Error relativo (%) = {erp:.4f} %")
    print("-" * 50)

# Casos de prueba
print("\n  CASOS DE PRUEBA")
esperados = [0.3, 0.2, 0.06]
for m, esp in zip(mediciones, esperados):
    erp = error_relativo(masa_real, m) * 100
    print(f"  Medición {m} kg -> ER(%) = {erp:.4f}")
