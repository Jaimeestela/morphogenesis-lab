# morphogenesis-lab

Laboratorio de morfogénesis para Rhino y Grasshopper. El mecanismo es el de Turing: dos sustancias que reaccionan y se difunden, un campo que se organiza en manchas o rayas, y unas curvas que siguen ese campo dentro de un rectángulo.

## Dónde se trabaja

| Carpeta | Uso |
| --- | --- |
| [grasshopper/](grasshopper/README.md) | Componentes GhPython. Es el camino de proyecto. |
| [matematicas/](matematicas/README.md) | Estudio del cálculo, de la rejilla a la curva, escrito para construirlo en Grasshopper. |
| [python/](python/README.md) | Scripts numéricos originales, con NumPy. Quedan como comprobación, no como interfaz. |

Empieza por [matematicas/01_rejilla.md](matematicas/01_rejilla.md) y por el montaje de [grasshopper/README.md](grasshopper/README.md).

## Qué se conserva del laboratorio

- Reacción-difusión en dos dimensiones: Gray-Scott, Schnakenberg y Brusselador.
- Estabilidad lineal del equilibrio homogéneo y modo dominante.
- Paso del campo a curvas que siguen la isolínea.
- Un serpentín regular para comparar esa trayectoria con una de ida y vuelta.

La formulación sigue a Turing (1952) como marco matemático. No se reproduce el texto del artículo. Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society of London B*, 237(641), 37–72.

## Licencia

MIT. Ver [LICENSE](LICENSE). Cita en [CITATION.cff](CITATION.cff).
