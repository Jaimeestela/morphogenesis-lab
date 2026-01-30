# MATLAB scripts (validación y prototipado)

## Cuándo usar MATLAB

1. **Validar estabilidad y modo dominante** rápidamente: barrido de k y autovalores de (J − k² D) sin depender del solver Python.
2. **Comprobar que el solver Python no se inventa dinámica**: comparar snapshots o evolución temporal con una implementación FD en MATLAB.
3. **Prototipar variantes de discretización**: probar esquemas (FD, FE) o condiciones de contorno antes de llevarlos a Python.

## Archivos

- **rd_fd_2d.m**: Simulación FD 2D básica (Laplaciano 5-point, Euler explícito) para un modelo (p. ej. Gray-Scott o Schnakenberg).
- **rd_stability_linear.m**: Cálculo de autovalores de (J − k² D) para un rango de k; devuelve el k que maximiza Re(λ).
- **rd_demo_patterns.m**: Script de demostración que llama a rd_fd_2d y opcionalmente rd_stability_linear, y guarda figuras.

## Cómo ejecutar

Desde MATLAB, en el directorio `matlab/`:

```matlab
rd_stability_linear   % barrido de k y modo dominante
rd_fd_2d             % una corrida FD 2D
rd_demo_patterns     % demo completa
```

## Validación cruzada con Python

- Comparar el `k` dominante devuelto por `rd_stability_linear.m` con `morphogenesis.stability.dominant_mode()`.
- Comparar un snapshot (u,v) de `rd_fd_2d.m` con el de `experiments/01_gray_scott_2d.py` (mismos parámetros y semilla si aplica).
