# Modelo matemático

## PDE reacción–difusión (2 especies)

En el dominio espacial Ω (2D) y tiempo t:

- ∂u/∂t = D_u ∇²u + f(u, v)
- ∂v/∂t = D_v ∇²v + g(u, v)

con:
- u, v: concentraciones (campos escalares).
- D_u, D_v: coeficientes de difusión (constantes).
- f, g: términos de reacción (no lineales).

## Equilibrio homogéneo

Punto (u₀, v₀) tal que f(u₀, v₀) = 0 y g(u₀, v₀) = 0. En el paper de Turing, la estabilidad de este equilibrio se analiza linealizando y estudiando modos espaciales.

## Linealización y modos

Perturbación (δu, δv) = (U, V) e^{i k·x + λ t}. Sustituyendo en las PDE linealizadas se obtiene el problema de autovalores:

- (J − k² D) (U, V)^T = λ (U, V)^T

con J = Jacobiano de (f,g) en (u₀,v₀) y D = diag(D_u, D_v). Si existe k ≠ 0 con Re(λ) > 0, el equilibrio homogéneo es inestable; el k que maximiza Re(λ) es el modo dominante.

## Modelos implementados

- **Gray-Scott**: f = −uv² + F(1−u), g = uv² − (F+k)v. Parámetros F, k.
- **Schnakenberg**: f = a − u + u²v, g = b − u²v. Equilibrio homogéneo (u₀,v₀) en función de a, b.
- **Brusselator**: f = a − (b+1)u + u²v, g = bu − u²v. Equilibrio (a, b/a); parámetros a, b.

Detalles de equilibrios y Jacobianos en `src/morphogenesis/rd_models.py` y en las notas `papers/notes/turing_key_equations.md`.
