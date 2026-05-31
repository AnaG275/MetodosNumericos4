# Error de Redondeo

## Definición
El Error de Redondeo ocurre cuando un número real se representa con una
cantidad limitada de cifras decimales o dígitos significativos. Este tipo
de error aparece porque las computadoras y las calculadoras no pueden
almacenar infinitos decimales, por lo que realizan aproximaciones.

Es uno de los errores más comunes en los métodos numéricos y puede
acumularse cuando se realizan muchas operaciones consecutivas.

---

## Fórmula

Error de Redondeo = |Valor Real − Valor Redondeado|

Donde:
- Valor Real         → número original antes del redondeo
- Valor Redondeado   → número aproximado después del redondeo
- | |                → valor absoluto

---

## Algoritmo

Obtener el valor real

Seleccionar el número de decimales deseado

Aplicar el redondeo al valor real

Calcular la diferencia entre el valor real y el valor redondeado

Obtener el valor absoluto de la diferencia

Mostrar el error obtenido

Interpretar el resultado:
entre menor sea el error de redondeo,
más cercana será la aproximación al valor original

---

## Ejemplo

Valor real = 5.678912

Redondeando a 3 decimales:

Valor redondeado = 5.679

Error de Redondeo = |5.678912 − 5.679|

Error de Redondeo = |-0.000088|

Error de Redondeo = 0.000088

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Valor real = 8.246753, redondeado a 2 decimales

| Dato | Valor |
|-------|---------|
| Valor real | 8.246753 |
| Valor redondeado | 8.250000 |
| Diferencia | 0.003247 |
| Error de redondeo | 0.003247 |

**Resultado:** `Error de Redondeo = 0.003247`

---

**Ejercicio:** Valor real = 3.14159265, redondeado a 4 decimales

| Dato | Valor |
|-------|---------|
| Valor real | 3.14159265 |
| Valor redondeado | 3.14160000 |
| Diferencia | 0.00000735 |
| Error de redondeo | 0.00000735 |

**Resultado:**
- Entrada: valor real = 3.14159265, decimales = 4
- Resultado esperado: 0.00000735
- Resultado float:    0.00000735
- Diferencia:         0.00000735
- Error acumulado:    0.00000000
