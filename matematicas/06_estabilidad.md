# 06. La estabilidad

Se perturba el equilibrio con una onda de número `k`:

`(δu, δv) = (U, V) exp(i k x + λ t)`

Al linealizar, cada `k` tiene una matriz de 2×2:

`M = J - k² D`

`J` es el jacobiano de `(f, g)` en el equilibrio. `D` es la diagonal `(Du, Dv)`. `λ` es el autovalor de `M`.

Si la parte real de `λ` es negativa para todo `k`, la mezcla uniforme vuelve a su sitio. Si para algún `k` distinto de cero esa parte real es positiva, esa longitud de onda crece. El `k` con la parte real más grande es el modo dominante. Su longitud aproximada en celdas es `2π / k`.

Para una matriz `[[a, b], [c, d]]` la parte real mayor, cuando el discriminante no es negativo, es:

`λ = (traza + raíz(traza² - 4 det)) / 2`

con `traza = a + d` y `det = a d - b c`. Antes de usar la fórmula, a `a` se le resta `k² Du` y a `d` se le resta `k² Dv`.

## En Grasshopper

`componente_estabilidad.py` devuelve `k_dominante` y `lambda_real`.

1. Deja Schnakenberg en `a = 0.1`, `b = 0.9`, `Du = 0.05`, `Dv = 1`.
2. Lee `lambda_real`. Con esos números es positivo y `k_dominante` queda cerca de 2.2. El capítulo 07 puede formar manchas.
3. Sube `Du` hasta que `lambda_real` pase a negativo. La simulación debe dejar de organizar el campo. Esa es la comprobación.

Los parámetros viejos del script NumPy (`a = 0.2`, `b = 1`, `Du = 0.001`, `Dv = 0.01`) dan `lambda_real` negativo. Conservarlos en `python/` no implica que el lienzo deba empezar por ellos.
