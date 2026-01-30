# Pipeline hacia CAD

## Idea principal

**Reacción–difusión → campo escalar → campo vectorial → streamlines → curvas CAD**

1. **Reacción–difusión**: Se simula un modelo (Gray-Scott, Schnakenberg, Brusselator) en 2D y se obtienen campos u(x,y), v(x,y) en un snapshot.
2. **Campo escalar**: Se define φ a partir de u/v (p. ej. φ = u, φ = v, o φ = u−v, etc.) sobre la malla.
3. **Campo vectorial**: Se obtiene **∇φ** (gradiente) o un campo rotado (p. ej. perpendicular para seguir isocontornos) en los puntos de la malla; se interpola si hace falta en puntos arbitrarios.
4. **Streamlines**: Se integran líneas de flujo del campo vectorial con paso fijo y separación mínima entre líneas; se hace **clipping** al dominio (polígono Shapely) y se respetan obstáculos (agujeros).
5. **Curvas CAD**: Las polilíneas resultantes se exportan a **DXF** (capas por estancia/colector/rutas) y **SVG** para inspección.

Así se generan trayectorias “tipo tuberías” o mecanizado que siguen la estructura del patrón.

## Alternativa: planner determinista (serpentine)

**Serpentine / boustrophedon por estancia → conexiones a colector**

- Por cada estancia (polígono): se rellena con un patrón en serpentina (ida y vuelta) con paso (pitch) y radio mínimo de curvatura fijados.
- Las estancias se conectan entre sí y a un **colector** mediante un grafo de rutas (corredores). Esto da un “circuito” por habitación más un árbol de conexión al colector.
- Este baseline es **determinista** y no depende del patrón RD; sirve para comparar calidad (longitud, cobertura, cruces) con el enfoque basado en streamlines.

## Criterios de evaluación

Para comparar y validar trayectorias (streamlines vs serpentine, o distintas semillas/parámetros):

| Criterio | Descripción |
|----------|-------------|
| **Longitud total** | Suma de longitudes de todas las polilíneas (por estancia y colector). |
| **Uniformidad de cobertura** | Distribución de distancias de puntos del dominio a la polilínea más cercana (histograma, desv. típica). |
| **Radios mínimos** | Mínimo radio de curvatura en esquinas; debe respetar un umbral (p. ej. para tuberías). |
| **Cruces** | Número de intersecciones entre segmentos (evitar cuando sea posible). |
| **Distancia a bordes** | Distancia mínima de la trayectoria al borde del dominio; debe ser ≥ margen. |
| **Número de bucles** | Cuenta de componentes conexas o bucles cerrados; relevante para circuitos de suelo radiante. |

Estos criterios se implementan o referencian en `src/morphogenesis/metrics.py` y en los experimentos de export (DXF/SVG).
