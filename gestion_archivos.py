"""
Operaciones de persistencia: creación de carpetas, lectura y escritura CSV.
"""

import os
import csv
from manejo_excepciones import ErrorArchivo


ENCABEZADOS = ["nombre", "estudio", "anio", "valoracion", "precio"]


def crear_directorio_si_no_existe(ruta):
    """Crea la ruta completa si no existe."""
    try:
        os.makedirs(ruta, exist_ok=True)
    except OSError as e:
        raise ErrorArchivo(f"Error creando directorio '{ruta}': {e}")


def obtener_ruta_csv(plataforma, categoria):
    """Devuelve la ruta al CSV correspondiente."""
    if not plataforma or not plataforma.strip():
        raise ValueError("La plataforma no puede estar vacía.")
    if not categoria or not categoria.strip():
        raise ValueError("La categoría no puede estar vacía.")
    base = os.path.join("data", plataforma.strip(), categoria.strip())
    crear_directorio_si_no_existe(base)
    return os.path.join(base, "juegos.csv")


def leer_csv(ruta_csv):
    """Lee un CSV y devuelve una lista de diccionarios."""
    juegos = []
    if not os.path.exists(ruta_csv):
        return juegos
    try:
        with open(ruta_csv, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                if all(k in fila for k in ENCABEZADOS):
                    juegos.append(fila)
    except (OSError, csv.Error) as e:
        raise ErrorArchivo(f"Error leyendo CSV '{ruta_csv}': {e}")
    return juegos


def sobrescribir_csv(ruta_csv, lista_juegos):
    """Sobrescribe el CSV con una nueva lista de juegos."""
    try:
        crear_directorio_si_no_existe(os.path.dirname(ruta_csv))
        with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            escritor.writeheader()
            filas = [{k: j.get(k, "") for k in ENCABEZADOS} for j in lista_juegos]
            escritor.writerows(filas)
    except (OSError, csv.Error) as e:
        raise ErrorArchivo(f"Error sobrescribiendo CSV '{ruta_csv}': {e}")
