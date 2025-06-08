from utils.obtener_palabras_limpias import obtener_palabras_limpias
from utils.quicksort import quicksort
from utils.busqueda_binaria_iterativa import busqueda_binaria_iterativa
def main(): 
    palabras = obtener_palabras_limpias()
    palabras_ordenadas = quicksort(palabras)
    print(palabras_ordenadas)
    objetivo = input("Ingrese la palabra que desea buscar: ")
    if not objetivo:
        print("No se ingresó ninguna palabra.")
        return
    indice = busqueda_binaria_iterativa(palabras_ordenadas, objetivo)
    if indice != -1:
        print(f"La palabra '{objetivo}' se encuentra en el índice {indice}.")
    else:
        print(f"La palabra '{objetivo}' no se encontró en la lista.")

if __name__ == "__main__":
    main()
