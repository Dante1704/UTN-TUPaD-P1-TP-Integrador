import time

def busqueda_nativa_python(lista, elemento):
    inicio = time.time()
    indice = lista.index(elemento)
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la búsqueda nativa: {duracion:.6f} segundos")
    return indice