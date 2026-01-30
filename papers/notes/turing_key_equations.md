# Ecuaciones clave (inspirado en Turing 1952)

Resumen de las ecuaciones y relaciones usadas en el repo. No es copia literal del paper; es una adaptación para implementación numérica.

## PDE reacción–difusión

- ∂u/∂t = D_u ∇²u + f(u,v)
- ∂v/∂t = D_v ∇²v + g(u,v)

## Gray-Scott

- f = −uv² + F(1−u),  g = uv² − (F+k)v
- Parámetros: F, k, D_u, D_v
- Equilibrio homogéneo trivial: (1, 0). Otros equilibrios y patrones dependen de F, k.

## Schnakenberg

- f = a − u + u²v,  g = b − u²v
- Equilibrio: u₀ = a + b, v₀ = b / (a+b)²
- Jacobiano en (u₀,v₀): J_11 = −1 + 2u₀v₀, J_12 = u₀², J_21 = −2u₀v₀, J_22 = −u₀²

## Brusselator

- f = a − (b+1)u + u²v,  g = bu − u²v
- Equilibrio: (u₀, v₀) = (a, b/a)
- Jacobiano: J_11 = b−1, J_12 = a², J_21 = −b, J_22 = −a²

## Estabilidad lineal (modo k)

- Matriz: M = J − k² D,  D = diag(D_u, D_v)
- Autovalores λ de M: si Re(λ) > 0 para algún k ≠ 0, equilibrio homogéneo inestable.
- Modo dominante: k que maximiza Re(λ).

Implementación numérica: `src/morphogenesis/rd_models.py`, `stability.py`.
