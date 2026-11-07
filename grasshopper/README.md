# Grasshopper

El laboratorio se trabaja aquí. Rhino 8 y un componente GhPython con Python 3.

La definición no está guardada como archivo binario `.gh`. Cada pieza es un script de esta carpeta, para que el cálculo se pueda leer y cambiar en Git. El lienzo se monta una vez y se vuelve a abrir desde tu archivo de Rhino.

## Preparar el componente

1. Abre Grasshopper dentro de Rhino 8.
2. Coloca un componente `GhPython Script` por cada script.
3. En cada uno, clic derecho, `Set Module Search Paths`, y añade la carpeta `grasshopper/ghpython` de este repositorio.
4. Copia el contenido del script en el componente.
5. Crea entradas y salidas con los nombres que indica la primera línea del archivo. Los nombres tienen que coincidir: `dominio`, `nx`, `campo`, `curvas`.

## Orden en el lienzo

1. `Rectangle`. Es el dominio. Conéctalo a todos los componentes que lo pidan.
2. Un modelo: `componente_gray_scott.py`, `componente_schnakenberg.py` o `componente_brusselator.py`.
3. Salidas `puntos`, `valores` y `malla` para ver el campo.
4. La salida `campo` entra en `componente_lineas_de_flujo.py`.
5. `componente_serpentin.py` usa solo el rectángulo. Es la trayectoria de comparación.
6. `componente_estabilidad.py` no necesita geometría. Devuelve `k_dominante` y `lambda_real` para Schnakenberg o el Brusselador.

## Qué hace cada archivo

| Archivo | Papel |
| --- | --- |
| `ghpython/nucleo.py` | Ecuaciones, laplaciano, estabilidad y curvas en índices. No importa Rhino. |
| `ghpython/geometria.py` | Pasa esos índices al rectángulo de Rhino. |
| `ghpython/componente_*.py` | El texto que va dentro de cada GhPython. |

El estudio que explica por qué este orden va de lo simple a lo complejo está en `matematicas/`.
