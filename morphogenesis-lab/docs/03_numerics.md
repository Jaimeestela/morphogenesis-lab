# Discretización y solvers

## Malla

- Dominio rectangular 2D discretizado en malla regular (nx × ny).
- Espaciado Δx, Δy (constantes).

## Laplaciano

- Diferencias finitas 5-point:  
  ∇²φ ≈ (φ_{i+1,j} + φ_{i-1,j} + φ_{i,j+1} + φ_{i,j-1} − 4φ_{i,j}) / h²  
  con h = Δx = Δy si malla cuadrada.

## Condiciones de contorno

- **Neumann (reflectante)**: derivada normal cero; se implementa con “ghost” cells o actualizando bordes para que el flujo sea nulo.
- **Dirichlet**: valores fijos en el borde (p. ej. equilibrio homogéneo).

## Integración temporal

- **Euler explícito**: u^{n+1} = u^n + Δt (D_u L[u^n] + f(u^n,v^n)), idem para v. Estabilidad: Δt limitado por CFL (difusión).
- **RK2 (opcional)**: paso intermedio y promediado para mejor precisión temporal.

## Semilla inicial

- Equilibrio homogéneo + perturbación aleatoria reproducible (semilla fija) para romper simetría y disparar inestabilidad.

## Output

- Campos u, v en cada paso (o en intervalos); snapshots guardados como arrays y/o imágenes (PNG).

Implementación: `src/morphogenesis/rd_solvers.py` y `grids.py`.
