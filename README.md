#  Proyecto Python Seguro - Unidad 1 - Tarea PPS05

##  Información General
Este repositorio contiene el aplicativo de gestión de caracteres desarrollado en la Unidad 1.
La estructura ha sido migrada a un entorno Git para garantizar el control de versiones y la integridad del código fuente.

- **Tecnologías:** Python 3.12.
- **Estructura:** Arquitectura modular con carpeta dedicada `/scripts`.
- **Plataforma:** Entorno de desarrollo seguro (Kali Linux).

##  Guía de despliegue
Para instalar y ejecutar este programa en un entorno local, siga estos pasos:

1. **Clonar el repositorio:**
   `git clone <url_del_repositorio>`
2. **Acceder al directorio:**
   `cd proyecto_python/scripts`
3. **Ejecutar el software:**
   `python3 mychar.py`

##  Tabla de Trazabilidad
| Versión | Fecha | Descripción de los cambios |
| :--- | :--- | :--- |
| 1.0 | 14/04/2026 | Inicialización del repositorio y migración de la carpeta de scripts. |

##  Checklist de Seguridad
Se han tomado decisiones técnicas para proteger el repositorio de la **exposición de información** (Information Leakage).
Se han identificado los siguientes elementos para ser protegidos/ignorados:

- **Ficheros de registro (*.log):** Para evitar que se filtren rutas del sistema o errores de depuración.
- **Entornos virtuales (.venv/):** Para no subir binarios locales y mantener el repositorio ligero.
- **Caché (__pycache__/):** Por higiene del repositorio y para evitar conflictos entre ejecuciones.
- **Bases de datos locales (*.sqlite3):** Para prevenir la fuga de datos volátiles de prueba.
