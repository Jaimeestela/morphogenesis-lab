# Scripts Python

Aquí queda el laboratorio numérico original: modelos de reacción-difusión, estabilidad lineal, líneas de flujo, serpentín y exportación DXF/SVG.

No es el camino de trabajo de Rhino. Ese camino está en `grasshopper/` y el estudio que lo explica está en `matematicas/`. Estos scripts sirven para comprobar cifras con NumPy y para repetir un experimento largo fuera de Grasshopper.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
python experiments/01_gray_scott_2d.py
```

Las notas de esta carpeta siguen en inglés porque son el archivo del prototipo numérico. El estudio dirigido a Grasshopper está escrito en castellano en la raíz del repositorio.
