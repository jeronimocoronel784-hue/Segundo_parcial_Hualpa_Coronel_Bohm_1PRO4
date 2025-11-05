"""
Operaciones CRUD sobre la lista de juegos en memoria.
"""

from manejo_excepciones import manejar_error, ErrorEntradaInvalida
from utilidades import validar_juego


@manejar_error
def agregar_juego():
    """Crea un nuevo juego y lo devuelve (no guarda todavía en disco)."""
    plataforma = input("Plataforma: ").strip()
    categoria = input("Categoría: ").strip()
    if not plataforma or not categoria:
        raise ErrorEntradaInvalida("Plataforma y categoría son obligatorias.")

    nombre = input("Nombre del juego: ")
    estudio = input("Estudio desarrollador: ")
    anio = input("Año de lanzamiento: ")
    valoracion = input("Valoración (0–10): ")
    precio = input("Precio en USD: ")

    juego = validar_juego(nombre, estudio, anio, valoracion, precio)
    juego["plataforma"] = plataforma
    juego["categoria"] = categoria
    print("Juego agregado a la memoria temporal.")
    return juego


@manejar_error
def modificar_juego(lista_juegos):
    """Modifica un juego existente dentro de la lista en memoria."""
    if not lista_juegos:
        print("No hay juegos cargados en memoria.")
        return
    nombre = input("Nombre del juego a modificar: ").strip()
    for j in lista_juegos:
        if j["nombre"].lower() == nombre.lower():
            campo = input("Campo a modificar (estudio, anio, valoracion, precio): ").strip()
            if campo not in ("estudio", "anio", "valoracion", "precio"):
                raise ErrorEntradaInvalida("Campo inválido.")
            nuevo_valor = input("Nuevo valor: ").strip()
            j[campo] = nuevo_valor
            validar_juego(j["nombre"], j["estudio"], j["anio"], j["valoracion"], j["precio"])
            print("Juego modificado en memoria.")
            return
    print("No se encontró el juego especificado.")


@manejar_error
def eliminar_juego(lista_juegos):
    """Elimina un juego de la lista en memoria."""
    if not lista_juegos:
        print("No hay juegos cargados en memoria.")
        return
    nombre = input("Nombre del juego a eliminar: ").strip()
    original = len(lista_juegos)
    lista_juegos[:] = [j for j in lista_juegos if j["nombre"].lower() != nombre.lower()]
    if len(lista_juegos) < original:
        print("Juego eliminado de la memoria temporal.")
    else:
        print("No se encontró el juego especificado.")
