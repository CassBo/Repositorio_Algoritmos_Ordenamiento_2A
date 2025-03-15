def quicksort(arr):

    # Llamada inicial al helper que implementa QuickSort
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, low, high):
    # Función helper que implementa QuickSort recursivamente

    if low < high:
        # Encuentra el índice del pivote (el elemento que estará en su posición final)
        pivot_index = partition(arr, low, high)

        # Llama recursivamente a quicksort para las sub-listas a la izquierda y a la derecha del pivote
        _quicksort(arr, low, pivot_index - 1)
        _quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Función para particionar el arreglo alrededor de un pivote

    # Selecciona el pivote (en este caso, el último elemento del rango)
    pivot = arr[high]

    # Índice del primer elemento que será mayor que el pivote
    i = low

    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote, lo intercambia con el elemento en arr[i]
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Coloca el pivote en su posición final intercambiándolo con el elemento en arr[i]
    arr[i], arr[high] = arr[high], arr[i]

    # Retorna el índice del pivote
    return i

# Ejemplo
arr = [6, 5, 3, 1, 8, 7, 2, 4]

# Llama a la función de ordenamiento QuickSort
quicksort(arr)

# Imprime la lista ordenada
print("Lista ordenada:", arr)