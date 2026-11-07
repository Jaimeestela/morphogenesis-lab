# 02. El laplaciano

La difusión mira la diferencia entre una celda y sus vecinas.

En una dimensión, la segunda derivada discreta es:

`(u[i+1] - 2 u[i] + u[i-1]) / dx²`

En la malla se suman la dirección `i` y la dirección `j`. Ese operador es el laplaciano de cinco puntos. Si la celda está en el borde, la vecina que faltaría repite el valor de la propia celda. Ese borde se llama Neumann: no entra ni sale materia por el contorno.

Si el laplaciano es positivo, la celda está en un valle y la difusión la rellena. Si es negativo, está en un pico y la difusión la vacía.

## En Grasshopper

No hace falta un componente solo para el laplaciano. Vive dentro de cada paso de `nucleo.py`, función `laplaciano`. Para verlo aislado, saca el campo `v` después de pocos pasos y compara una celda con la media de sus cuatro vecinas. Esa diferencia, partida por `dx²`, es el término de difusión.
