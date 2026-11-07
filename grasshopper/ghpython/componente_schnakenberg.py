"""Componente GhPython. Schnakenberg.

Entradas: dominio, nx, ny, pasos, a, b, Du, Dv, dt, semilla
Salidas: puntos, valores, malla, campo
Valores por defecto: a 0.1, b 0.9, Du 0.05, Dv 1, dt 0.02, pasos 600.
Con estos números el modo dominante es inestable. Los del script NumPy antiguo pueden no serlo.
"""

import nucleo
import geometria

nx = 32 if "nx" not in globals() or nx is None else int(nx)
ny = 32 if "ny" not in globals() or ny is None else int(ny)
pasos = 600 if "pasos" not in globals() or pasos is None else int(pasos)
a = 0.1 if "a" not in globals() or a is None else float(a)
b = 0.9 if "b" not in globals() or b is None else float(b)
Du = 0.05 if "Du" not in globals() or Du is None else float(Du)
Dv = 1.0 if "Dv" not in globals() or Dv is None else float(Dv)
dt = 0.02 if "dt" not in globals() or dt is None else float(dt)
semilla = 42 if "semilla" not in globals() or semilla is None else int(semilla)

u0, v0 = nucleo.equilibrio_schnakenberg(a, b)
u, v = nucleo.sembrar_equilibrio(nx, ny, u0, v0, 0.02, semilla)

def un_paso(uu, vv):
    return nucleo.paso_schnakenberg(uu, vv, a, b, Du, Dv, 1.0, 1.0, dt)

u, v = nucleo.simular(un_paso, u, v, pasos)
minimo, maximo = geometria.limites(dominio)
puntos, valores = geometria.puntos_de_campo(u, minimo, maximo)
malla = geometria.malla_de_campo(u, minimo, maximo)
campo = u
