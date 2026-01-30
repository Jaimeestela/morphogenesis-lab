# morphogenesis-lab

Repositorio de laboratorio para **reacción–difusión tipo Turing** y generación de geometría CAD a partir de patrones: validación numérica del núcleo del paper de Turing (1952), extracción de trayectorias (streamlines, serpentine) y export a DXF/SVG.

## Qué es este repositorio

- **Reproducción y validación numérica** del mecanismo central del artículo de Turing (1952): sistemas de reacción–difusión y formación de patrón por **inestabilidad del equilibrio homogéneo** (linealización + simulación no lineal), en 2D.
- **Pipeline hacia CAD**: convertir patrones/campos en geometría útil: trayectorias tipo mecanizado, tuberías o suelo radiante dentro de dominios 2D (plantas), con vistas a 3D (superficies, losas).
- **Diseñado para iterar con LLMs** (GPT, Cursor): experimentos reproducibles, métricas y flujo “paper → prototipo”.

La conexión con el paper de Turing es conceptual y matemática: usamos el mismo marco (PDE reacción–difusión, linealización en torno al equilibrio, difusión que desestabiliza y selecciona una longitud de onda). No copiamos texto literal; véase [docs/01_turing_summary.md](docs/01_turing_summary.md).

---

## Qué parte reproduce de Turing

- **Modelo**: dos especies (u, v) con reacción no lineal y difusión (coeficientes Du, Dv). Ecuaciones tipo  
  `∂u/∂t = Du ∇²u + f(u,v)`, `∂v/∂t = Dv ∇²v + g(u,v)`.
- **Inestabilidad del equilibrio homogéneo**: linealización en (u₀, v₀); para cada modo espacial k, se estudia el operador lineal `J - k² D`. Bajo ciertos parámetros, la difusión desestabiliza el equilibrio y aparece un **modo dominante** (k que maximiza Re(λ)).
- **Simulación no lineal**: integración temporal en malla 2D (FD 5-point) para ver patrones tipo “ondas estacionarias” (manchas, rayas, etc.).

Implementamos **Gray-Scott**, **Schnakenberg** y **Brusselator** como modelos estándar y un módulo de **estabilidad lineal** para estimar el modo dominante sin simular.

---

## Instalación

### Con Conda (recomendado)

```bash
cd morphogenesis-lab
conda env create -f environment.yml
conda activate morphogenesis-lab
pip install -e .
```

### Con venv

```bash
cd morphogenesis-lab
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

---

## Cómo ejecutar experimentos

```bash
# Patrones 2D (Gray-Scott, Schnakenberg, Brusselator)
python experiments/01_gray_scott_2d.py
python experiments/02_schnakenberg_2d.py
python experiments/03_brusselator_2d.py

# De patrón RD → streamlines → DXF/SVG
python experiments/10_rd_to_streamlines.py

# Serpentine por estancias + colector (dominio multi-estancia)
python experiments/11_rd_to_serpentine_rooms.py

# Export DXF directo
python experiments/12_export_dxf.py
```

Los resultados se escriben en `data/outputs/patterns/`, `data/outputs/paths/` y `data/outputs/exports/`.

---

## Outputs que produce

- **Imágenes de patrón**: PNG de snapshots u/v (y opcionalmente mapa de color) en `data/outputs/patterns/`.
- **Arrays**: numpy (`.npy`) o similar para reproducir o post-procesar.
- **Trayectorias**: polilíneas (streamlines o serpentine) exportadas a **DXF** (capas por estancia/colector/rutas) y **SVG** para inspección rápida en `data/outputs/exports/`.

---

## Roadmap por hitos

| Hito | Descripción |
|------|-------------|
| **1** | Patrones 2D estables reproducibles (Gray-Scott, Schnakenberg, Brusselator) y validación con análisis de estabilidad lineal. |
| **2** | Extracción de trayectorias: campo escalar → vectorial → streamlines con separación mínima y clipping a dominio; export DXF/SVG. |
| **3** | Multi-estancia con colector: dominio por estancias (GeoJSON), serpentine por habitación y grafo de rutas hacia colector. |
| **4** | Salto a 3D: superficies, losas y export mesh (STL/STEP) para integración futura en FreeCAD/LignumBIM. |

---

## Primeros 3 comandos para empezar

```bash
conda activate morphogenesis-lab
python experiments/00_smoke_test.py
python experiments/01_gray_scott_2d.py
```

Luego revisa `data/outputs/patterns/` para los PNG del patrón.

---

## Qué mirar en los outputs

- **`data/outputs/patterns/`**: PNG de u/v en distintos tiempos; comprueba que no hay explosión numérica (valores finitos) y que el patrón es estable.
- **`data/outputs/paths/`**: geometrías intermedias (listas de puntos) si se guardan.
- **`data/outputs/exports/`**: DXF y SVG; ábrelos en un visor o CAD para comprobar capas, longitud y que las líneas no salen del dominio.

---

## Siguientes pasos para integrar en FreeCAD/LignumBIM (futuro)

- Importar DXF en FreeCAD como croquis o geometría 2D y extrudir/barrido para tuberías o losas.
- Definir convenciones de capas (estancia, colector, rutas) compatibles con flujos BIM.
- Exportar mallas 3D (STL) o STEP desde `mesh_export` para análisis estructural o fabricación.

---

## Documentación

- [docs/00_context.md](docs/00_context.md) — Contexto del proyecto.
- [docs/01_turing_summary.md](docs/01_turing_summary.md) — Resumen técnico del paper de Turing e ideas reutilizables.
- [docs/02_math_model.md](docs/02_math_model.md) — Modelo matemático.
- [docs/03_numerics.md](docs/03_numerics.md) — Discretización y solvers.
- [docs/04_cad_pipeline.md](docs/04_cad_pipeline.md) — Pipeline reacción–difusión → CAD y criterios de evaluación.
- [docs/05_experiments.md](docs/05_experiments.md) — Descripción de experimentos.
- [docs/06_results_log.md](docs/06_results_log.md) — Registro de resultados.

---

## Licencia

MIT. Ver [LICENSE](LICENSE).

## Citar

Ver [CITATION.cff](CITATION.cff). Para el paper original: Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society of London B*, 237(641), 37–72.
