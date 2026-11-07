# 08. Del campo a la curva

El patrón sigue siendo números. La geometría de obra es una curva.

El gradiente `(∂φ/∂x, ∂φ/∂y)` señala hacia donde el campo crece. La dirección perpendicular `(-∂φ/∂y, ∂φ/∂x)` camina a lo largo de una isolínea. Esa es la línea de flujo que usa el laboratorio: una trayectoria que sigue el dibujo, como un tubo o un mecanizado que no corta el patrón a través.

Se siembran puntos cada ciertas celdas y se avanza con paso fijo hasta salir del dominio o hasta agotar la longitud.

El serpentín es la comparación. Es una ida y vuelta con separación constante. No mira el campo. Sirve para medir si las líneas del patrón cubren mejor o peor que una trayectoria regular: longitud, distancia al borde, cruces.

## En Grasshopper

1. Conecta la salida `campo` del componente del modelo a `componente_lineas_de_flujo.py`.
2. El mismo `dominio` entra en los dos.
3. En paralelo, `componente_serpentin.py` con el mismo rectángulo.
4. Las dos salidas `curvas` se pueden hornear o medir con `Length`.

`paso` está en celdas, no en metros. `0.5` recorre media celda por iteración. Si las curvas se salen o tiemblan, bájalo. Si quedan cortas, sube `longitud`.
