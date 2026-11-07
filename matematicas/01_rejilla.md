# 01. Una rejilla

Un patrón no es una superficie. Es una tabla de números.

Se parte el rectángulo de Rhino en `nx` por `ny` celdas. Cada celda guarda dos cantidades, `u` y `v`. En el modelo son dos sustancias. En el dibujo serán el color de un punto.

La posición de la celda `(i, j)` dentro del rectángulo es solo un traslado:

- `x = x_min + (x_max - x_min) * i / (nx - 1)`
- `y = y_min + (y_max - y_min) * j / (ny - 1)`

El cálculo del patrón no usa metros. Usa el índice de la celda y un paso numérico `dx = 1`. El rectángulo de Rhino solo coloca el resultado. Así el mismo patrón cabe en una baldosa o en una losa sin cambiar la ecuación.

## En Grasshopper

1. Un `Rectangle` es el dominio.
2. El componente `componente_gray_scott.py` lee esa caja y devuelve un punto por celda.
3. La salida `valores` es el número de cada celda. `Gradient` o un círculo de radio proporcional a `valores` lo hace visible.

Antes de simular, comprueba solo esto: `nx * ny` puntos, ordenados, dentro del rectángulo.
