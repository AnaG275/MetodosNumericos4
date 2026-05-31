# ============================================================
# TEMA: Error Absoluto
# EJERCICIO 3: Medición de temperatura
# ============================================================
# Un termómetro marca 36.5°C pero la temperatura real es 36.8°C

def error_absoluto(real, medido):
    return abs(real - medido)

casos = [
    (36.8, 36.5, "Termómetro 1"),
    (100.0, 99.3, "Termómetro 2 (ebullición)"),
    (0.0, 0.2,   "Termómetro 3 (fusión)"),
]

print("=" * 50)
print("  ERROR ABSOLUTO - Mediciones de Temperatura")
print("=" * 50)
for real, medido, nombre in casos:
    ea = error_absoluto(real, medido)
    print(f"\n  {nombre}")
    print(f"    Temperatura real   : {real} °C")
    print(f"    Temperatura medida : {medido} °C")
    print(f"    Error absoluto     : {ea:.4f} °C")

print("\n" + "=" * 50)
print("  CASOS DE PRUEBA")
print("=" * 50)
assert round(error_absoluto(36.8, 36.5), 4) == 0.3,   "Fallo caso 1"
assert round(error_absoluto(100.0, 99.3), 4) == 0.7,  "Fallo caso 2"
assert round(error_absoluto(0.0, 0.2), 4) == 0.2,     "Fallo caso 3"
print("  Todos los casos de prueba pasaron correctamente.")
