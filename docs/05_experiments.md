# Descripción de experimentos

## Smoke test

- **`experiments/00_smoke_test.py`**: Importa el paquete, ejecuta una mini-simulación (pocos pasos) y comprueba que no hay NaNs. Sirve para validar instalación.

## Patrones 2D

- **`01_gray_scott_2d.py`**: Gray-Scott en malla 2D; parámetros para patrón estable; guarda snapshots PNG y arrays en `data/outputs/patterns/`.
- **`02_schnakenberg_2d.py`**: Schnakenberg; idem.
- **`03_brusselator_2d.py`**: Brusselator; idem.

## Pipeline RD → trayectorias

- **`10_rd_to_streamlines.py`**: Carga un snapshot u/v (o genera uno), construye φ, deriva campo vectorial, genera streamlines dentro de un polígono (Shapely), exporta DXF y SVG a `data/outputs/exports/`.
- **`11_rd_to_serpentine_rooms.py`**: Dominio multi-estancia (p. ej. desde `data/domains/simple_rooms.geojson`); genera serpentine por estancia y grafo de rutas al colector; exporta DXF/SVG con capas por estancia/colector/rutas.
- **`12_export_dxf.py`**: Prueba directa de export DXF (polilíneas de ejemplo o salida de 10/11) con capas.

## Reproducibilidad

- Semillas fijas (numpy.random.seed) donde aplique.
- Parámetros en cabecera del script o en `config.py` para poder variar desde un solo lugar.
- Logging básico y rutas de salida en `data/outputs/`.
