# 03. La reacción

La difusión sola alisa. El dibujo aparece porque las dos sustancias reaccionan.

Hay dos campos y dos leyes, `f(u, v)` y `g(u, v)`.

Gray-Scott:

- `f = -u v² + F (1 - u)`
- `g = u v² - (F + k) v`

`F` alimenta `u`. `k` retira `v`. El término `u v²` es el encuentro de las dos.

Schnakenberg:

- `f = a - u + u² v`
- `g = b - u² v`

Brusselador:

- `f = a - (b + 1) u + u² v`
- `g = b u - u² v`

Los tres comparten la forma de Turing: producción local más difusión. Cambian los parámetros, no la estructura del componente.

## En Grasshopper

Un componente por modelo:

- `componente_gray_scott.py`
- `componente_schnakenberg.py`
- `componente_brusselator.py`

Empieza por Gray-Scott con `F = 0.03` y `k = 0.062`. Es el caso que el laboratorio numérico ya usaba.
