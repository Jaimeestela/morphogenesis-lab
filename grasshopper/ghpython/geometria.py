"""Pasa la malla numérica al rectángulo de Rhino.

Grasshopper inyecta `Rhino`. Este módulo solo se importa dentro de un componente.
"""

import Rhino.Geometry as rg


def limites(dominio):
    caja = dominio.GetBoundingBox(True)
    return caja.Min, caja.Max


def a_punto(i, j, nx, ny, minimo, maximo):
    tx = 0.0 if nx <= 1 else i / float(nx - 1)
    ty = 0.0 if ny <= 1 else j / float(ny - 1)
    x = minimo.X + (maximo.X - minimo.X) * tx
    y = minimo.Y + (maximo.Y - minimo.Y) * ty
    return rg.Point3d(x, y, minimo.Z)


def puntos_de_campo(campo, minimo, maximo):
    ny = len(campo)
    nx = len(campo[0])
    puntos = []
    valores = []
    for j in range(ny):
        for i in range(nx):
            puntos.append(a_punto(i, j, nx, ny, minimo, maximo))
            valores.append(campo[j][i])
    return puntos, valores


def curvas_de_indices(curvas, nx, ny, minimo, maximo):
    salida = []
    for curva in curvas:
        polilinea = rg.Polyline()
        for x, y in curva:
            polilinea.Add(a_punto(x, y, nx, ny, minimo, maximo))
        if polilinea.Count > 1:
            salida.append(polilinea.ToNurbsCurve())
    return salida


def malla_de_campo(campo, minimo, maximo):
    ny = len(campo)
    nx = len(campo[0])
    malla = rg.Mesh()
    for j in range(ny):
        for i in range(nx):
            malla.Vertices.Add(a_punto(i, j, nx, ny, minimo, maximo))
    for j in range(ny - 1):
        for i in range(nx - 1):
            a = i + j * nx
            b = a + 1
            c = a + nx
            d = c + 1
            malla.Faces.AddFace(a, b, d, c)
    malla.Normals.ComputeNormals()
    malla.Compact()
    return malla
