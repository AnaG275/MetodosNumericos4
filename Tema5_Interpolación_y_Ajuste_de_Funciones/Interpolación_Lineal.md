# Interpolación Lineal

## Definición
La Interpolación Lineal es un método numérico utilizado para estimar el
valor de una función entre dos puntos conocidos. Asume que la variación
entre los puntos puede aproximarse mediante una línea recta, por lo que
es uno de los métodos de interpolación más simples y utilizados.

Su precisión es adecuada cuando los datos presentan un comportamiento
aproximadamente lineal en el intervalo considerado.

---

## Fórmula

P(x) = y₀ + [(y₁ - y₀)/(x₁ - x₀)] · (x - x₀)

Donde:
- (x₀, y₀) → primer punto conocido
- (x₁, y₁) → segundo punto conocido
- x        → valor donde se desea interpolar
- P(x)     → valor aproximado obtenido

---

## Algoritmo

Definir dos puntos conocidos

Identificar el valor x donde se desea interpolar

Calcular la pendiente de la recta:

m = (y₁ - y₀)/(x₁ - x₀)

Sustituir los valores en la fórmula de interpolación

Realizar las operaciones correspondientes

Obtener el valor aproximado P(x)

Mostrar el resultado

---

## Ejemplo

Puntos conocidos:

(2, 5) y (6, 13)

Interpolar en:

x = 4

Tabla de datos:

| Punto | x | y |
|--------|----|----|
| P₀ | 2 | 5 |
| P₁ | 6 | 13 |

Aplicando la fórmula:

P(4) = 5 + [(13 - 5)/(6 - 2)](4 - 2)

P(4) = 5 + (8/4)(2)

P(4) = 5 + 4

P(4) = 9

---

## Ejemplo y Caso de Prueba

**Caso de prueba:**

Puntos:

(1,3) y (5,11)

Interpolar en x = 3

| Punto | x | y |
|--------|----|----|
| P₀ | 1 | 3 |
| P₁ | 5 | 11 |

**Resultado:** `P(3) = 7.0000`

---

**Ejercicio:**

Puntos:

(4,10) y (8,22)

Interpolar en x = 6

| Punto | x | y |
|--------|----|----|
| P₀ | 4 | 10 |
| P₁ | 8 | 22 |

**Resultado:**
- Entrada: (4,10), (8,22), x = 6
- Resultado esperado: 16.0000
- Resultado float:    16.0000
- Método utilizado:   Interpolación Lineal
- Error acumulado:    0.0000
