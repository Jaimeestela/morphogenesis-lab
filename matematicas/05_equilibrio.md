# 05. El equilibrio

El equilibrio homogéneo es el par `(u0, v0)` en el que la reacción se anula en todas las celdas, sin difusión:

- `f(u0, v0) = 0`
- `g(u0, v0) = 0`

Schnakenberg: `u0 = a + b`, `v0 = b / (a + b)²`.

Brusselador: `u0 = a`, `v0 = b / a`.

Gray-Scott tiene un equilibrio trivial `(1, 0)`. Ahí no hay patrón: `v` es cero y la reacción de `v` también. El dibujo de Gray-Scott no sale de romper ese equilibrio con una onda pequeña. Sale de una semilla finita, el bloque central del componente.

## En Grasshopper

`componente_estabilidad.py` usa el equilibrio de Schnakenberg o del Brusselador. Gray-Scott no entra en ese componente. Si quieres el patrón de Gray-Scott, siembra y simula. Si quieres saber si un parámetro es inestable antes de simular, cambia de modelo.
