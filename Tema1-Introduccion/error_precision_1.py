# ============================================================
# TEMA: Error de Precisión
# EJERCICIO 1: Comparación float32 vs float64
# ============================================================
import numpy as np

x = 1.0 / 3.0

f32 = np.float32(x)
f64 = np.float64(x)
valor_ref = x  # Python usa float64 nativo

print("=" * 55)
print("  ERROR DE PRECISIÓN - float32 vs float64")
print("=" * 55)
print(f"  Valor de referencia (Python float): {valor_ref:.20f}")
print(f"  float32 : {float(f32):.20f}")
print(f"  float64 : {float(f64):.20f}")
print(f"\n  Error float32 : {abs(float(f32) - valor_ref):.2e}")
print(f"  Error float64 : {abs(float(f64) - valor_ref):.2e}")

# Acumulación de errores
n = 1000
suma32 = np.float32(0.0)
suma64 = np.float64(0.0)
paso   = 1.0 / n

for _ in range(n):
    suma32 += np.float32(paso)
    suma64 += np.float64(paso)

print(f"\n  Suma de {n} pasos de 1/{n}:")
print(f"    float32 = {float(suma32):.15f}  error = {abs(1.0 - float(suma32)):.2e}")
print(f"    float64 = {float(suma64):.15f}  error = {abs(1.0 - float(suma64)):.2e}")

# Casos de prueba
print("\n  CASOS DE PRUEBA")
assert abs(float(f32) - valor_ref) > abs(float(f64) - valor_ref), "float64 debe ser más preciso"
print("  float64 es más preciso que float32. OK")
