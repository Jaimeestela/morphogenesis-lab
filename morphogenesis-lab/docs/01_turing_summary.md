# Resumen técnico del paper de Turing (1952)

Este documento resume las ideas centrales del artículo **“The chemical basis of morphogenesis”** (Turing, 1952). El repositorio usa el paper como inspiración conceptual y matemática; no se copia texto literal.

## Resumen en 1–2 páginas

Turing propone que patrones espaciales en sistemas biológicos (p. ej. manchas, rayas) pueden surgir por **inestabilidad de un equilibrio homogéneo** en un sistema de reacción–difusión con dos (o más) morfógenos. La idea clave: en un sistema solo con reacción, el equilibrio homogéneo puede ser estable; al añadir **difusión con coeficientes distintos** para cada especie, el operador lineal que gobierna las perturbaciones puede volverse inestable para ciertos modos espaciales. Así, la difusión “desestabiliza” el estado uniforme y selecciona una **longitud de onda** (o modo dominante) que da lugar al patrón.

- **Modelo**: PDE de reacción–difusión para dos concentraciones u, v:
  - ∂u/∂t = D_u ∇²u + f(u,v)
  - ∂v/∂t = D_v ∇²v + g(u,v)
  con f, g no lineales.

- **Equilibrio homogéneo**: (u₀, v₀) tal que f(u₀,v₀)=0, g(u₀,v₀)=0.

- **Linealización**: Se perturba (u,v) = (u₀,v₀) + (δu, δv). En espacio de Fourier (modo e^{ik·x}), el crecimiento de la perturbación viene gobernado por los autovalores de la matriz **J − k² D**, donde J es el Jacobiano de (f,g) en (u₀,v₀) y D = diag(D_u, D_v). Si para algún k ≠ 0 la parte real de un autovalor es > 0, el equilibrio homogéneo es inestable frente a ese modo.

- **Modo dominante**: El k (o longitud de onda) que maximiza Re(λ) es el que crece más rápido y suele determinar la escala del patrón (“ondas estacionarias” en 2D).

- **Simulación no lineal**: Integrar las PDE en 2D con condiciones de contorno adecuadas produce patrones (manchas, rayas, etc.) coherentes con el análisis lineal.

## Ideas reutilizables en este repo

| Idea | Uso en el repo |
|------|-----------------|
| Modelo reacción–difusión (PDE) | Gray-Scott, Schnakenberg, Brusselator en `rd_models.py`; solver 2D en `rd_solvers.py`. |
| Linealización en torno al equilibrio y criterio de inestabilidad (modo/longitud de onda dominante) | `stability.py`: cálculo numérico de autovalores de (J − k² D) y búsqueda del k dominante. |
| Interpretación de patrones como “ondas estacionarias” y generalización a 2D | Patrones 2D en malla regular; snapshots y análisis de escala. |

## Qué NO copiamos y qué adaptamos

- **No copiamos**: texto largo literal del paper; demostraciones formales; notación exacta de Turing.
- **Adaptamos a ingeniería/CAD**: los campos u/v (o funciones de ellos) se usan como **campos escalares** para derivar trayectorias (streamlines, isocontornos) y generar geometría (polilíneas DXF/SVG) para tuberías, suelo radiante, etc. El criterio de estabilidad lineal se usa para elegir parámetros y escala de patrón antes de simular.

## Referencia

Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society of London B*, 237(641), 37–72. DOI: 10.1098/rstb.1952.0012.
