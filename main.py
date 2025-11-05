"""
Archivo principal del sistema de gestión de videojuegos.
Contiene el menú principal y las opciones de manejo de datos en memoria
y persistencia condicional (guardar al salir o descartar cambios).
"""

from manejo_excepciones import manejar_error
from crud import agregar_juego, modificar_juego, eliminar_juego
from recursividad import leer_directorio_recursivo
from gestion_archivos import sobrescribir_csv, obtener_ruta_csv
from utilidades import ordenar_juegos, calcular_estadisticas



@manejar_error
def cargar_datos_en_memoria():
    """Carga todos los juegos existentes desde los CSV hacia memoria."""
    global juegos_en_memoria
    juegos_en_memoria = leer_directorio_recursivo()
    print(f"Datos cargados en memoria ({len(juegos_en_memoria)} registros).")


@manejar_error
def mostrar_juegos():
    """Muestra los juegos actualmente en memoria."""
    if not juegos_en_memoria:
        print("No hay juegos cargados en memoria.")
        return
    print(f"\nTotal de juegos en memoria: {len(juegos_en_memoria)}\n")
    for j in juegos_en_memoria:
        print(f"{j.get('plataforma')} → {j.get('categoria')} → {j.get('nombre')} "
            f"({j.get('anio')}) - {j.get('estudio')} - Valoración: {j.get('valoracion')} - Precio: ${j.get('precio')}")


@manejar_error
def opcion_ordenar():
    """Permite ordenar los juegos actualmente en memoria."""
    if not juegos_en_memoria:
        print("No hay juegos cargados.")
        return
    clave1 = input("Ordenar por atributo principal: ").strip()
    clave2 = input("Atributo secundario (opcional): ").strip() or None
    ordenados = ordenar_juegos(juegos_en_memoria, clave1, clave2)
    for j in ordenados:
        print(f"{j.get('nombre')} ({j.get('anio')}) - Valoración: {j.get('valoracion')} - Precio: ${j.get('precio')}")


@manejar_error
def opcion_estadisticas():
    """Calcula y muestra estadísticas globales sobre los juegos en memoria."""
    if not juegos_en_memoria:
        print("No hay datos para analizar.")
        return
    estad = calcular_estadisticas(juegos_en_memoria)
    if estad:
        print(f"Total de juegos: {estad['total']}")
        print(f"Promedio de valoración: {estad['promedio_valoracion']}")
        print(f"Promedio de precio: ${estad['promedio_precio']}")
        print("Cantidad por plataforma:")
        for plat, cnt in estad["conteo_por_plataforma"].items():
            print(f"  {plat}: {cnt}")


@manejar_error
def guardar_cambios():
    """Guarda todos los juegos en memoria en sus respectivos CSV."""
    if not juegos_en_memoria:
        print("No hay datos en memoria para guardar.")
        return
    print("Guardando datos en disco...")
    # Agrupar juegos por plataforma y categoría para escribirlos en los CSV correspondientes
    estructura = {}
    for j in juegos_en_memoria:
        plat = j.get("plataforma")
        cat = j.get("categoria")
        estructura.setdefault((plat, cat), []).append(j)
    for (plat, cat), lista in estructura.items():
        ruta_csv = obtener_ruta_csv(plat, cat)
        sobrescribir_csv(ruta_csv, lista)
    print("Cambios guardados correctamente.")


def menu():
    cargar_datos_en_memoria()

    while True:
        print("\n=== GESTIÓN DE VIDEOJUEGOS ===")
        print("1. Agregar nuevo juego")
        print("2. Mostrar juegos en memoria")
        print("3. Modificar juego")
        print("4. Eliminar juego")
        print("5. Ordenar juegos")
        print("6. Ver estadísticas globales")
        print("7. Guardar y salir")
        print("8. Salir sin guardar")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nuevo = agregar_juego()
            if nuevo:
                juegos_en_memoria.append(nuevo)
        elif opcion == "2":
            mostrar_juegos()
        elif opcion == "3":
            modificar_juego(juegos_en_memoria)
        elif opcion == "4":
            eliminar_juego(juegos_en_memoria)
        elif opcion == "5":
            opcion_ordenar()
        elif opcion == "6":
            opcion_estadisticas()
        elif opcion == "7":
            guardar_cambios()
            print("Saliendo del sistema (datos guardados).")
            break
        elif opcion == "8":
            confirmar = input("¿Seguro que desea salir sin guardar? (s/n): ").strip().lower()
            if confirmar == "s":
                print("Saliendo sin guardar cambios...")
                break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
