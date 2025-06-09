from utils.obtener_palabras_limpias import obtener_palabras_limpias
from utils.busqueda_nativa_python import busqueda_nativa_python

from utils.quicksort import quicksort
from utils.busqueda_binaria_iterativa import busqueda_binaria_iterativa
def main(): 
    palabras = obtener_palabras_limpias()
    palabras_ordenadas = quicksort(palabras)
    palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")
    objetivo = palabra_a_buscar.lower()
    if not objetivo:
        print("No se ingresó ninguna palabra. No se realizará la búsqueda.")
        return
    indice = busqueda_binaria_iterativa(palabras_ordenadas, objetivo)
    indice_2 = busqueda_nativa_python(palabras_ordenadas, objetivo)
    if indice != -1 or indice_2 != -1:
        print(f"La palabra '{palabra_a_buscar}' está presente en el archivo")
    else:
        print(f"La palabra '{palabra_a_buscar}' no se encontró en el archivo.")

if __name__ == "__main__":
    main()
