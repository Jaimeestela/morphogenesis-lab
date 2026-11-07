"""Componente GhPython. Del campo a curvas.

Entradas:
  dominio
  campo    rejilla de nucleo (lista de filas) o, si no llega, se calcula un Gray-Scott corto
  nx, ny   solo si el campo no llega ya creado
  paso     avance de la curva en celdas, por defecto 0.5
  longitud pasos máximos de cada curva, por defecto 80
  cada     separación entre semillas, en celdas, por defecto 6

Salidas: curvas
Las curvas siguen la isolínea, perpendiculares al gradiente.
"""

import nucleo
import geometria

paso = 0.5 if "paso" not in globals() or paso is None else float(paso)
longitud = 80 if "longitud" not in globals() or longitud is None else int(longitud)
cada = 6 if "cada" not in globals() or cada is None else int(cada)

if "campo" not in globals() or campo is None:
    nx = 48 if "nx" not in globals() or nx is None else int(nx)
    ny = 48 if "ny" not in globals() or ny is None else int(ny)
    u, v = nucleo.sembrar_gray_scott(nx, ny, 42)

    def un_paso(uu, vv):
        return nucleo.paso_gray_scott(uu, vv, 0.03, 0.062, 0.0002, 0.0001, 1.0, 1.0, 0.5)

    u, campo = nucleo.simular(un_paso, u, v, 300)

ny = len(campo)
nx = len(campo[0])
semillas = []
for j in range(cada, ny - cada, cada):
    for i in range(cada, nx - cada, cada):
        semillas.append((float(i), float(j)))

indices = nucleo.lineas_de_nivel(campo, 1.0, 1.0, semillas, paso, longitud)
minimo, maximo = geometria.limites(dominio)
curvas = geometria.curvas_de_indices(indices, nx, ny, minimo, maximo)
