# 04. El paso de tiempo

En cada celda, el cambio en un instante es difusión más reacción:

- `u_nuevo = u + dt (Du · laplaciano(u) + f)`
- `v_nuevo = v + dt (Dv · laplaciano(v) + g)`

`Du` y `Dv` dicen cuánto viaja cada sustancia. Si son distintos, una se escapa más deprisa que la otra. Ese desequilibrio es la condición de Turing.

`dt` no es un parámetro de diseño. Si es demasiado grande, el número se dispara. Si el campo deja de ser finito, baja `dt` antes de tocar `F` o `k`.

Los valores de partida, los mismos del script numérico, son:

| Modelo | Du | Dv | dt |
| --- | --- | --- | --- |
| Gray-Scott | 0.0002 | 0.0001 | 0.5 |
| Schnakenberg | 0.05 | 1 | 0.02 |
| Brusselador | 0.008 | 0.08 | 0.01 |

## En Grasshopper

`pasos` es cuántas veces se aplica la fórmula. Con 50 pasos se ve la semilla. Con 400 empieza el patrón. Sube de cien en cien y mira si el dibujo se asienta o sigue moviéndose.
