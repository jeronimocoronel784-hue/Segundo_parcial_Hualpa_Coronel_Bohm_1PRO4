"""
Módulo central de manejo de excepciones.

Define:
- Excepciones personalizadas.
- Decorador @manejar_error para manejo global de errores.
"""

import csv
import os
import traceback
from functools import wraps


class ErrorEntradaInvalida(Exception):
    """Error para entradas inválidas por parte del usuario."""
    pass


class ErrorArchivo(Exception):
    """Error para problemas con archivos o directorios."""
    pass


def manejar_error(func):
    """
    Decorador que encapsula el manejo de errores de alto nivel.
    Muestra mensajes controlados y evita que el programa se interrumpa.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ErrorEntradaInvalida as e:
            print(f"Error de entrada: {e}")
        except FileNotFoundError as e:
            print(f"Archivo no encontrado: {e}")
        except ErrorArchivo as e:
            print(f"Error de archivo: {e}")
        except (OSError, csv.Error) as e:
            print(f"Error al manipular archivos: {e}")
        except ValueError as e:
            print(f"Error de validación: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Detalles técnicos:")
            traceback.print_exc(limit=1)
        return None
    return wrapper


def asegurar_ruta_existente(ruta):
    """Lanza ErrorArchivo si la ruta no existe."""
    if not os.path.exists(ruta):
        raise ErrorArchivo(f"La ruta no existe: {ruta}")
