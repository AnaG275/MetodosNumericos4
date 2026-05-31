# ============================================================
# TEMA: Error Relativo
# EJERCICIO 1: Longitud de un puente
# ============================================================
# Medición real vs medición aproximada de la longitud de un puente

def error_relativo(real, aprox):
    return abs(real - aprox) / abs(real)

def error_relativo_porcentaje(real, aprox):
    return error_relativo(real, aprox) * 100

valor_real = 250.0   # metros
valor_aprox = 248.5  # metros

ea  = abs(valor_real - valor_aprox)
er  = error_relativo(valor_real, valor_aprox)
erp = error_relativo_porcentaje(valor_real, valor_aprox)

print("=" * 50)
print("  ERROR RELATIVO - Longitud de un puente")
print("=" * 50)
print(f"  Longitud real      : {valor_real} m")
print(f"  Longitud medida    : {valor_aprox} m")
print(f"  Error absoluto     : {ea:.4f} m")
print(f"  Error relativo     : {er:.6f}")
print(f"  Error relativo (%) : {erp:.4f} %")
print("=" * 50)

# Casos de prueba
casos = [
    (250.0, 248.5),
    (1000.0, 998.0),
    (50.0, 49.5),
]
print("\n  CASOS DE PRUEBA")
for r, a in casos:
    er = error_relativo_porcentaje(r, a)
    print(f"  Real={r}, Aprox={a} -> ER = {er:.4f} %")
