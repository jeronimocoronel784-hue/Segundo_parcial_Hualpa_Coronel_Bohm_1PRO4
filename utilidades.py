"""
Validaciones, ordenamientos y estadísticas de videojuegos.
"""

from manejo_excepciones import ErrorEntradaInvalida


def validar_texto(campo, valor):
    if not valor or not valor.strip():
        raise ErrorEntradaInvalida(f"El campo '{campo}' no puede estar vacío.")
    return valor.strip()


def validar_juego(nombre, estudio, anio, valoracion, precio):
    nombre = validar_texto("nombre", nombre)
    estudio = validar_texto("estudio", estudio)

    try:
        anio_int = int(anio)
        if anio_int < 1950 or anio_int > 2100:
            raise ErrorEntradaInvalida("El año debe estar entre 1950 y 2100.")
    except ValueError:
        raise ErrorEntradaInvalida("El año debe ser un número entero válido.")

    try:
        val = float(valoracion)
        if not (0 <= val <= 10):
            raise ErrorEntradaInvalida("La valoración debe estar entre 0 y 10.")
    except ValueError:
        raise ErrorEntradaInvalida("Valoración inválida.")

    try:
        precio_f = float(precio)
        if precio_f <= 0:
            raise ErrorEntradaInvalida("El precio debe ser positivo.")
    except ValueError:
        raise ErrorEntradaInvalida("Precio inválido.")

    return {
        "nombre": nombre,
        "estudio": estudio,
        "anio": str(anio_int),
        "valoracion": str(val),
        "precio": str(precio_f)
    }


def ordenar_juegos(juegos, clave1, clave2=None):
    if not juegos:
        return []
    return sorted(juegos, key=lambda j: (j.get(clave1, ""), j.get(clave2, "")))


def calcular_estadisticas(juegos):
    if not juegos:
        return None
    total = len(juegos)
    promedio_val = sum(float(j["valoracion"]) for j in juegos) / total
    promedio_precio = sum(float(j["precio"]) for j in juegos) / total
    conteo = {}
    for j in juegos:
        plat = j.get("plataforma", "Desconocida")
        conteo[plat] = conteo.get(plat, 0) + 1
    return {
        "total": total,
        "promedio_valoracion": round(promedio_val, 2),
        "promedio_precio": round(promedio_precio, 2),
        "conteo_por_plataforma": conteo
    }
