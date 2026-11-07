"""Componente GhPython. Gray-Scott.

Entradas:
  dominio  rectángulo, curva o cualquier geometría con caja
  nx       enteros de la malla, por defecto 48
  ny       por defecto 48
  pasos    por defecto 400
  F        alimentación, por defecto 0.03
  k        desaparición, por defecto 0.062
  Du       por defecto 0.0002
  Dv       por defecto 0.0001
  dt       por defecto 0.5
  semilla  por defecto 42

Salidas: puntos, valores, malla, campo
El valor de salida es la especie v, la que dibuja el patrón.
`campo` es la rejilla que alimenta las líneas de flujo.
"""

import nucleo
import geometria

nx = 48 if "nx" not in globals() or nx is None else int(nx)
ny = 48 if "ny" not in globals() or ny is None else int(ny)
pasos = 400 if "pasos" not in globals() or pasos is None else int(pasos)
F = 0.03 if "F" not in globals() or F is None else float(F)
k = 0.062 if "k" not in globals() or k is None else float(k)
Du = 0.0002 if "Du" not in globals() or Du is None else float(Du)
Dv = 0.0001 if "Dv" not in globals() or Dv is None else float(Dv)
dt = 0.5 if "dt" not in globals() or dt is None else float(dt)
semilla = 42 if "semilla" not in globals() or semilla is None else int(semilla)

u, v = nucleo.sembrar_gray_scott(nx, ny, semilla)

def un_paso(uu, vv):
    return nucleo.paso_gray_scott(uu, vv, F, k, Du, Dv, 1.0, 1.0, dt)

u, v = nucleo.simular(un_paso, u, v, pasos)
minimo, maximo = geometria.limites(dominio)
puntos, valores = geometria.puntos_de_campo(v, minimo, maximo)
malla = geometria.malla_de_campo(v, minimo, maximo)
campo = v
