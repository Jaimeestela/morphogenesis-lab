# 07. El patrón

La simulación repite el paso de tiempo sobre la semilla.

En Gray-Scott la semilla es un bloque central con `u ≈ 0.5` y `v ≈ 0.25` dentro de un campo `(1, 0)`. En Schnakenberg y en el Brusselador la semilla es el equilibrio más un ruido pequeño.

Lo que se dibuja es un instante del campo, no la ecuación. Manchas, rayas o laberinto dependen de `F`, `k`, `a`, `b` y de la razón `Du/Dv`. No dependan del tamaño del rectángulo de Rhino.

## En Grasshopper

1. `Rectangle`.
2. `componente_gray_scott.py` con las entradas nombradas igual que el archivo.
3. Salida `malla` a un componente de preview. El valor de color puede salir de `valores` con `Bounds` y `Gradient`.
4. Repite con Schnakenberg solo cuando el capítulo 06 haya dado `lambda_real` positivo.

La malla tiene un vértice por celda. No es una isosuperficie. Es la tabla del capítulo 01 puesta en el rectángulo.
