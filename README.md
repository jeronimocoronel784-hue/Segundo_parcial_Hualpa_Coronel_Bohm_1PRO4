#  Gestión Jerárquica de Videojuegos

Segundo Parcial Hualpa – Programación I – Jerónimo Coronel - Nicolas Bohm - 1PRO4

---

##  Descripción

Este proyecto implementa un sistema completo de gestión de videojuegos utilizando **Python**.
Los datos se almacenan en una estructura **jerárquica de carpetas y archivos CSV**, representando plataformas y categorías.
Incluye manejo de archivos, recursividad, validaciones, excepciones y guardado condicional.
---

## Video explicativo

https://drive.google.com/file/d/1f7394GZ-3-GlCiCEeMjpCs3Zg03SrQ6-/view?usp=sharing
---

##  Estructura jerárquica

```
data/
├── PC/
│   ├── Accion/juegos.csv
│   └── RPG/juegos.csv
└── Nintendo Switch/
    └── Aventura/juegos.csv
```

Cada CSV contiene las columnas:
| nombre | estudio | año | valoración | precio |

---

##  Módulos principales

| Archivo                 | Descripción                                          |
| ----------------------- | ---------------------------------------------------- |
| `main.py`               | Menú principal, carga en memoria y guardado opcional |
| `crud.py`               | Operaciones CRUD sobre la lista en memoria           |
| `gestion_archivos.py`   | Lectura y escritura de archivos CSV                  |
| `recursividad.py`       | Lectura recursiva de directorios                     |
| `utilidades.py`         | Validaciones, ordenamiento y estadísticas            |
| `manejo_excepciones.py` | Decorador global y manejo de errores personalizados  |

---

##  Funcionalidades

* Agregar, modificar y eliminar videojuegos.
* Leer todos los archivos CSV recursivamente.
* Calcular estadísticas globales (promedio de valoración y precio).
* Ordenar los datos por uno o más campos.
* Guardar los cambios o salir sin guardar.
* Función de carga de datos de ejemplo (comentada por defecto).

---

##  Ejecución

1. Ejecutar `main.py`
2. (Opcional) Descomentar la función `crear_csv_demo()` para crear datos de muestra.
3. Navegar por el menú interactivo desde consola.

---

##  Ejemplo de uso

```
=== GESTIÓN DE VIDEOJUEGOS ===
1. Agregar nuevo juego
2. Mostrar juegos
3. Modificar juego
4. Eliminar juego
5. Ordenar juegos
6. Ver estadísticas
7. Guardar y salir
8. Salir sin guardar
```

---

##  Ejemplo de estadísticas

```
Total de juegos: 3
Promedio de valoración: 9.0
Promedio de precio: 63.32
Cantidad por plataforma:
  PC: 2
  Nintendo Switch: 1
```

---

##  Conceptos aplicados

* Modularización avanzada
* Recursividad
* Manejo de archivos CSV
* Estructuras jerárquicas con `os`
* Validaciones y manejo de excepciones
* Persistencia condicional

---

