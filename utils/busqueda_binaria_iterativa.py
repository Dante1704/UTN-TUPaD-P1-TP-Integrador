import time

def busqueda_binaria_iterativa(lista, objetivo):
    inicio = time.time()
    izquierda, derecha = 0, len(lista) - 1
    resultado = -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            resultado = medio
            break
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la búsqueda binaria con ordenamiento quicksort: {duracion:.6f} segundos")
    return resultado