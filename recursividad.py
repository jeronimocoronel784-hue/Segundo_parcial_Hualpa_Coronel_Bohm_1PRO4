"""
Lectura recursiva de la jerarquía de directorios 'data'.
"""

import os
from gestion_archivos import leer_csv


def leer_directorio_recursivo(ruta_base="data"):
    """Lee recursivamente todos los CSV dentro de 'data/'."""
    juegos_totales = []
    if not os.path.exists(ruta_base):
        return juegos_totales
    try:
        for elemento in os.listdir(ruta_base):
            ruta_completa = os.path.join(ruta_base, elemento)
            if os.path.isdir(ruta_completa):
                juegos_totales.extend(leer_directorio_recursivo(ruta_completa))
            elif elemento.lower().endswith(".csv"):
                juegos = leer_csv(ruta_completa)
                for j in juegos:
                    partes = ruta_completa.split(os.sep)
                    j["plataforma"] = partes[-3] if len(partes) >= 3 else "Desconocida"
                    j["categoria"] = partes[-2] if len(partes) >= 2 else "Desconocida"
                    juegos_totales.append(j)
    except PermissionError:
        pass
    return juegos_totales
