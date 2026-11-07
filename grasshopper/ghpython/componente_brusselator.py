"""Componente GhPython. Brusselador.

Entradas: dominio, nx, ny, pasos, a, b, Du, Dv, dt, semilla
Salidas: puntos, valores, malla, campo
Valores por defecto: a 1, b 2.5, Du 0.008, Dv 0.08, dt 0.01, pasos 400.
"""

import nucleo
import geometria

nx = 40 if "nx" not in globals() or nx is None else int(nx)
ny = 40 if "ny" not in globals() or ny is None else int(ny)
pasos = 400 if "pasos" not in globals() or pasos is None else int(pasos)
a = 1.0 if "a" not in globals() or a is None else float(a)
b = 2.5 if "b" not in globals() or b is None else float(b)
Du = 0.008 if "Du" not in globals() or Du is None else float(Du)
Dv = 0.08 if "Dv" not in globals() or Dv is None else float(Dv)
dt = 0.01 if "dt" not in globals() or dt is None else float(dt)
semilla = 42 if "semilla" not in globals() or semilla is None else int(semilla)

u0, v0 = nucleo.equilibrio_brusselator(a, b)
u, v = nucleo.sembrar_equilibrio(nx, ny, u0, v0, 0.02, semilla)

def un_paso(uu, vv):
    return nucleo.paso_brusselator(uu, vv, a, b, Du, Dv, 1.0, 1.0, dt)

u, v = nucleo.simular(un_paso, u, v, pasos)
minimo, maximo = geometria.limites(dominio)
puntos, valores = geometria.puntos_de_campo(u, minimo, maximo)
malla = geometria.malla_de_campo(u, minimo, maximo)
campo = u
