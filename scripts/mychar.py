# ============================================
# Archivo: mychar.py
# Descripción: Devuelve la cadena más larga de una lista de cadenas.
# Autor: Alumno D. José Luis Cabañas Cabañas
# Fecha: 27/10/2025
# Versión: 1.0
# ============================================

# Función para encontrar la cadena más larga

def cadena_mas_larga(lista):
    """
    Devuelve la cadena más larga de una lista de cadenas.
    Si hay varias con la misma longitud máxima, devuelve la primera en orden alfabético.
    Si la lista está vacía, devuelve una cadena vacía.
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista de cadenas.")
    
    if not lista:
        return ""

    # Verificamos que todos los elementos sean cadenas
    for elemento in lista:
        if not isinstance(elemento, str):
            raise ValueError("Todos los elementos de la lista deben ser cadenas de texto.")
    
    # Calculamos la longitud máxima
    longitud_max = max(len(cadena) for cadena in lista)

    # Filtramos solo las cadenas de esa longitud máxima
    candidatas = [cadena for cadena in lista if len(cadena) == longitud_max]

    # Devolvemos la primera en orden alfabético
    return sorted(candidatas)[0]

# Bloque principal para interacción con el usuario
if __name__ == "__main__":
    print("Introduce 5 palabras para determinar cuál es la más larga:\n")
    palabras = []

    for i in range(5):
        palabra = input(f"Palabra {i+1}: ").strip()
        palabras.append(palabra)

    resultado = cadena_mas_larga(palabras)
    print(f"\nLa palabra más larga es: '{resultado}'")
# Versión 1.0
