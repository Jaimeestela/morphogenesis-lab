"""Componente GhPython. Serpentín de comparación.

Entradas: dominio, nx, ny, margen, separacion
Salidas: curvas
No usa el patrón de Turing. Sirve para comparar una trayectoria regular con las líneas del campo.
"""

import nucleo
import geometria

nx = 48 if "nx" not in globals() or nx is None else int(nx)
ny = 48 if "ny" not in globals() or ny is None else int(ny)
margen = 2 if "margen" not in globals() or margen is None else int(margen)
separacion = 4 if "separacion" not in globals() or separacion is None else int(separacion)

indices = nucleo.serpentin(nx, ny, margen, separacion)
minimo, maximo = geometria.limites(dominio)
curvas = geometria.curvas_de_indices(indices, nx, ny, minimo, maximo)
