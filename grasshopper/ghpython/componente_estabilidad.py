"""Componente GhPython. Modo dominante, sin simular el tiempo.

Entradas:
  modelo   texto: schnakenberg o brusselator
  a, b, Du, Dv
Salidas: k_dominante, lambda_real
Si lambda_real es positivo, la difusión puede desestabilizar el equilibrio homogéneo.
Gray-Scott no entra aquí: su equilibrio trivial (1, 0) es estable y el patrón nace de una semilla finita.
"""

import nucleo

modelo = "schnakenberg" if "modelo" not in globals() or not modelo else str(modelo).lower()
a = 0.1 if "a" not in globals() or a is None else float(a)
b = 0.9 if "b" not in globals() or b is None else float(b)
Du = 0.05 if "Du" not in globals() or Du is None else float(Du)
Dv = 1.0 if "Dv" not in globals() or Dv is None else float(Dv)

if modelo.startswith("b"):
    matriz = nucleo.jacobiano_brusselator(a, b)
else:
    matriz = nucleo.jacobiano_schnakenberg(a, b)

k_dominante, lambda_real = nucleo.modo_dominante(matriz, Du, Dv)
