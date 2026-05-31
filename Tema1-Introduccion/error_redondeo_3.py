# ============================================================
# TEMA: Error de Redondeo
# EJERCICIO 3: Precisión en representación de decimales
# ============================================================
# 0.1 + 0.2 != 0.3 en punto flotante IEEE 754

print("=" * 55)
print("  ERROR DE REDONDEO - Representación decimal IEEE 754")
print("=" * 55)

a = 0.1
b = 0.2
c = 0.3
suma = a + b

print(f"\n  a = 0.1 almacenado como: {a:.20f}")
print(f"  b = 0.2 almacenado como: {b:.20f}")
print(f"  c = 0.3 almacenado como: {c:.20f}")
print(f"\n  a + b         = {suma:.20f}")
print(f"  c             = {c:.20f}")
print(f"  ¿a + b == c?  = {a + b == c}")
print(f"  Error redondeo= {abs(suma - c):.2e}")

# Solución recomendada con round()
print(f"\n  Con round(a+b, 10) == round(c, 10): {round(suma,10) == round(c,10)}")

# Casos de prueba con tolerancia
print("\n  CASOS DE PRUEBA (comparación con tolerancia)")
pares = [(0.1 + 0.2, 0.3), (0.7 + 0.1, 0.8), (1.0/3.0, 0.3333333333)]
for calc, esp in pares:
    er = abs(calc - esp)
    ok = er < 1e-10
    print(f"  calc={calc:.15f}, esp={esp:.15f} -> Error={er:.2e} [{'OK' if ok else 'REVISAR'}]")
