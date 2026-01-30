# Cursor: de RD a trayectorias

## Objetivo

Extraer trayectorias (streamlines y serpentine) a partir de patrones RD o de un planner determinista, dentro de dominios 2D (polígonos).

## Tareas

1. **streamline.py**: Campo escalar φ → grad(φ) o rotado; generación de streamlines con paso fijo y separación mínima; clipping a polígono Shapely; obstáculos (agujeros).
2. **serpentine.py**: Relleno boustrophedon por estancia (pitch, radio mínimo, offset); grafo de rutas que conecta estancias a un colector (corredores).
3. Integrar con snapshot u/v: en 10_rd_to_streamlines usar φ = u o v (o combinación) y exportar DXF/SVG.
4. Experimento 11: dominio multi-estancia (GeoJSON), serpentine por habitación + colector.

## Criterios

- Trayectorias no salen del dominio (tests de validez).
- Separación mínima entre líneas respetada donde se especifique.
- Export DXF con capas por estancia/colector/rutas.
