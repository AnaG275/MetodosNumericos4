# ============================================================
# TEMA: Error de Precisión
# EJERCICIO 3: Límite de precisión de la máquina (epsilon)
# ============================================================
import sys
import numpy as np

print("=" * 60)
print("  ERROR DE PRECISIÓN - Epsilon de máquina")
print("=" * 60)

# Epsilon de máquina: menor número positivo tal que 1 + eps != 1
eps_python = sys.float_info.epsilon
eps_f32    = np.finfo(np.float32).eps
eps_f64    = np.finfo(np.float64).eps

print(f"\n  Epsilon de máquina (Python float / float64):")
print(f"    sys.float_info.epsilon = {eps_python:.6e}")
print(f"    np.float32 eps         = {eps_f32:.6e}")
print(f"    np.float64 eps         = {eps_f64:.6e}")

# Cálculo manual del epsilon
print("\n  Cálculo manual de epsilon:")
eps = 1.0
while 1.0 + eps != 1.0:
    eps_anterior = eps
    eps /= 2.0
print(f"    Epsilon calculado = {eps_anterior:.6e}")

# Demostración
print("\n  Demostración:")
print(f"    1.0 + eps/2 == 1.0 ? {1.0 + eps_python/2 == 1.0}")
print(f"    1.0 + eps   == 1.0 ? {1.0 + eps_python == 1.0}")
print(f"    1.0 + eps*2 == 1.0 ? {1.0 + eps_python*2 == 1.0}")

# Casos de prueba
print("\n  CASOS DE PRUEBA")
assert 1.0 + eps_python / 2 == 1.0,  "eps/2 debe ser indistinguible"
assert 1.0 + eps_python * 2 != 1.0,  "eps*2 debe ser distinguible"
assert eps_f32 > eps_f64,             "float32 debe tener mayor epsilon"
print("  Todos los casos de prueba pasaron. OK")
