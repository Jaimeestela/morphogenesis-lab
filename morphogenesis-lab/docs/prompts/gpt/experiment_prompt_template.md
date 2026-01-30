# Plantilla de prompt para experimentos (GPT)

## Plantilla

```
Experimento: [nombre, p. ej. Gray-Scott 2D con parámetros X]
Objetivo: [qué se quiere validar o producir]
Parámetros:
  - [param1]: valor
  - [param2]: valor
  - semilla: [entero o "random"]
Outputs esperados:
  - [ruta relativa, p. ej. data/outputs/patterns/gs_snapshot_001.png]
Criterios de éxito:
  - [p. ej. no NaNs, patrón estable, DXF con N capas]
```

## Ejemplo

```
Experimento: Gray-Scott 2D spots
Objetivo: Generar patrón de manchas estable y guardar snapshots.
Parámetros:
  - F: 0.03
  - k: 0.062
  - Du, Dv: 0.0002, 0.0001
  - nx, ny: 256, 256
  - pasos: 10000
  - semilla: 42
Outputs esperados:
  - data/outputs/patterns/gs_u_*.png, gs_v_*.png
Criterios de éxito:
  - max(u), max(v) finitos; patrón visual de manchas.
```
