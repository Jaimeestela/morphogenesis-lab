"""Núcleo de morfogenia para Grasshopper.

Funciones puras, sin Rhino y sin NumPy, para poder pegarlas en GhPython.
La malla numérica no usa las unidades del modelo: el rectángulo de Rhino
solo sirve para colocar el resultado.
"""


def rejilla(nx, ny, valor):
    return [[valor for _ in range(nx)] for _ in range(ny)]


def copiar(campo):
    return [fila[:] for fila in campo]


def laplaciano(campo, dx, dy):
    """Laplaciano de cinco puntos con borde de Neumann: fuera de la malla se repite el valor del borde."""
    ny = len(campo)
    nx = len(campo[0])
    inv_dx2 = 1.0 / (dx * dx)
    inv_dy2 = 1.0 / (dy * dy)
    salida = rejilla(nx, ny, 0.0)
    for j in range(ny):
        for i in range(nx):
            centro = campo[j][i]
            derecha = campo[j][i + 1] if i + 1 < nx else centro
            izquierda = campo[j][i - 1] if i > 0 else centro
            arriba = campo[j + 1][i] if j + 1 < ny else centro
            abajo = campo[j - 1][i] if j > 0 else centro
            salida[j][i] = (derecha - 2.0 * centro + izquierda) * inv_dx2
            salida[j][i] += (arriba - 2.0 * centro + abajo) * inv_dy2
    return salida


def _ruido(semilla):
    estado = int(semilla) % 2147483647
    if estado <= 0:
        estado = 1

    def siguiente():
        nonlocal estado
        estado = (1103515245 * estado + 12345) % 2147483647
        return estado / 2147483647.0

    return siguiente


def sembrar_gray_scott(nx, ny, semilla):
    """Estado de reposo (1, 0) con un bloque central que dispara el patrón."""
    u = rejilla(nx, ny, 1.0)
    v = rejilla(nx, ny, 0.0)
    ruido = _ruido(semilla)
    i0, i1 = nx // 2 - nx // 10, nx // 2 + nx // 10
    j0, j1 = ny // 2 - ny // 10, ny // 2 + ny // 10
    for j in range(max(0, j0), min(ny, j1)):
        for i in range(max(0, i0), min(nx, i1)):
            u[j][i] = 0.50 + 0.02 * (ruido() - 0.5)
            v[j][i] = 0.25 + 0.02 * (ruido() - 0.5)
    return u, v


def sembrar_equilibrio(nx, ny, u0, v0, amplitud, semilla):
    ruido = _ruido(semilla)
    u = rejilla(nx, ny, 0.0)
    v = rejilla(nx, ny, 0.0)
    for j in range(ny):
        for i in range(nx):
            u[j][i] = u0 + amplitud * (ruido() - 0.5)
            v[j][i] = v0 + amplitud * (ruido() - 0.5)
    return u, v


def paso_gray_scott(u, v, f_feed, k, du, dv, dx, dy, dt):
    lap_u = laplaciano(u, dx, dy)
    lap_v = laplaciano(v, dx, dy)
    ny = len(u)
    nx = len(u[0])
    u2 = rejilla(nx, ny, 0.0)
    v2 = rejilla(nx, ny, 0.0)
    for j in range(ny):
        for i in range(nx):
            uu = u[j][i]
            vv = v[j][i]
            uvv = uu * vv * vv
            reaccion_u = -uvv + f_feed * (1.0 - uu)
            reaccion_v = uvv - (f_feed + k) * vv
            u2[j][i] = uu + dt * (du * lap_u[j][i] + reaccion_u)
            v2[j][i] = vv + dt * (dv * lap_v[j][i] + reaccion_v)
    return u2, v2


def equilibrio_schnakenberg(a, b):
    u0 = a + b
    return u0, b / (u0 * u0)


def paso_schnakenberg(u, v, a, b, du, dv, dx, dy, dt):
    lap_u = laplaciano(u, dx, dy)
    lap_v = laplaciano(v, dx, dy)
    ny = len(u)
    nx = len(u[0])
    u2 = rejilla(nx, ny, 0.0)
    v2 = rejilla(nx, ny, 0.0)
    for j in range(ny):
        for i in range(nx):
            uu = u[j][i]
            vv = v[j][i]
            uuv = uu * uu * vv
            u2[j][i] = uu + dt * (du * lap_u[j][i] + (a - uu + uuv))
            v2[j][i] = vv + dt * (dv * lap_v[j][i] + (b - uuv))
    return u2, v2


def equilibrio_brusselator(a, b):
    return a, b / a


def paso_brusselator(u, v, a, b, du, dv, dx, dy, dt):
    lap_u = laplaciano(u, dx, dy)
    lap_v = laplaciano(v, dx, dy)
    ny = len(u)
    nx = len(u[0])
    u2 = rejilla(nx, ny, 0.0)
    v2 = rejilla(nx, ny, 0.0)
    for j in range(ny):
        for i in range(nx):
            uu = u[j][i]
            vv = v[j][i]
            uuv = uu * uu * vv
            u2[j][i] = uu + dt * (du * lap_u[j][i] + (a - (b + 1.0) * uu + uuv))
            v2[j][i] = vv + dt * (dv * lap_v[j][i] + (b * uu - uuv))
    return u2, v2


def simular(paso, u, v, pasos):
    for _ in range(int(pasos)):
        u, v = paso(u, v)
    return u, v


def jacobiano_schnakenberg(a, b):
    u0, v0 = equilibrio_schnakenberg(a, b)
    return (
        (-1.0 + 2.0 * u0 * v0, u0 * u0),
        (-2.0 * u0 * v0, -(u0 * u0)),
    )


def jacobiano_brusselator(a, b):
    u0, v0 = equilibrio_brusselator(a, b)
    return (
        (b - 1.0 + 2.0 * u0 * v0, u0 * u0),
        (-b - 2.0 * u0 * v0, -(u0 * u0)),
    )


def autovalor_mayor(matriz, k2, du, dv):
    """Mayor parte real del autovalor de J - k² D, con D diagonal."""
    a, b = matriz[0]
    c, d = matriz[1]
    a = a - k2 * du
    d = d - k2 * dv
    traza = a + d
    determinante = a * d - b * c
    discriminante = traza * traza - 4.0 * determinante
    if discriminante >= 0.0:
        raiz = discriminante ** 0.5
        return 0.5 * (traza + raiz)
    return 0.5 * traza


def modo_dominante(matriz, du, dv, k_min=0.0, k_max=20.0, n_k=200):
    mejor_k = k_min
    mejor_lambda = autovalor_mayor(matriz, k_min * k_min, du, dv)
    paso = (k_max - k_min) / float(n_k - 1)
    for n in range(n_k):
        k = k_min + n * paso
        valor = autovalor_mayor(matriz, k * k, du, dv)
        if valor > mejor_lambda:
            mejor_lambda = valor
            mejor_k = k
    return mejor_k, mejor_lambda


def gradiente(campo, dx, dy):
    ny = len(campo)
    nx = len(campo[0])
    gx = rejilla(nx, ny, 0.0)
    gy = rejilla(nx, ny, 0.0)
    for j in range(ny):
        for i in range(nx):
            if 0 < i < nx - 1:
                gx[j][i] = (campo[j][i + 1] - campo[j][i - 1]) / (2.0 * dx)
            elif i == 0:
                gx[j][i] = (campo[j][1] - campo[j][0]) / dx
            else:
                gx[j][i] = (campo[j][nx - 1] - campo[j][nx - 2]) / dx
            if 0 < j < ny - 1:
                gy[j][i] = (campo[j + 1][i] - campo[j - 1][i]) / (2.0 * dy)
            elif j == 0:
                gy[j][i] = (campo[1][i] - campo[0][i]) / dy
            else:
                gy[j][i] = (campo[ny - 1][i] - campo[ny - 2][i]) / dy
    return gx, gy


def _muestra(campo, x, y):
    ny = len(campo)
    nx = len(campo[0])
    i = int(x)
    j = int(y)
    if i < 0:
        i = 0
    if j < 0:
        j = 0
    if i > nx - 1:
        i = nx - 1
    if j > ny - 1:
        j = ny - 1
    return campo[j][i]


def lineas_de_nivel(campo, dx, dy, semillas, paso, longitud):
    """Curvas que siguen la isolínea: perpendiculares al gradiente."""
    gx, gy = gradiente(campo, dx, dy)
    curvas = []
    for x0, y0 in semillas:
        for signo in (1.0, -1.0):
            curva = [(x0, y0)]
            x, y = x0, y0
            for _ in range(int(longitud)):
                vx = -signo * _muestra(gy, x, y)
                vy = signo * _muestra(gx, x, y)
                modulo = (vx * vx + vy * vy) ** 0.5
                if modulo < 1e-8:
                    break
                x += paso * vx / modulo
                y += paso * vy / modulo
                if x < 1 or y < 1 or x > len(campo[0]) - 2 or y > len(campo) - 2:
                    break
                curva.append((x, y))
            if len(curva) > 2:
                curvas.append(curva)
    return curvas


def serpentin(nx, ny, margen, separacion):
    """Ida y vuelta dentro del índice de la malla. No depende del patrón."""
    if separacion < 1:
        separacion = 1
    curvas = []
    y = margen
    direccion = 1
    while y < ny - margen:
        x0 = margen
        x1 = nx - 1 - margen
        if direccion > 0:
            curvas.append([(x0, y), (x1, y)])
        else:
            curvas.append([(x1, y), (x0, y)])
        y_siguiente = y + separacion
        if y_siguiente < ny - margen:
            curvas.append([(curvas[-1][1][0], y), (curvas[-1][1][0], y_siguiente)])
        y = y_siguiente
        direccion *= -1
    return curvas
