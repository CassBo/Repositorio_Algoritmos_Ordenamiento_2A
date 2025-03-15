import time
import numpy as np
import matplotlib.pyplot as plt

def selection_sort(A):
    for i in range(len(A)):  # Recorremos toda la lista
        minimo = i  # Suponemos que el mínimo está en i
        for j in range(i + 1, len(A)):  # Buscamos el menor en el resto de la lista
            if A[j] < A[minimo]:  # Corregimos la comparación
                minimo = j  # Actualizamos la posición del mínimo

        # Intercambiamos el elemento actual con el mínimo encontrado
        A[i], A[minimo] = A[minimo], A[i]
    return A

def best_case(n):
    return list(range(n))  # El mejor caso es la lista ordenada

def worst_case(n):
    return list(range(n, 0, -1))  # El peor caso es la lista en orden descendente

def average_case(n):
    return np.random.permutation(n).tolist()  # Caso promedio, permutación aleatoria

sizes = list(range(10, 501, 10))
best_times = []
worst_times = []
average_times = []

for n in sizes:
    # Mejor caso
    best_time = []
    best_input = best_case(n)
    for _ in range(10):
        start = time.time()
        selection_sort(best_input)
        end = time.time()
        best_time.append(end - start)
    best_times.append(np.mean(best_time))

    # Peor caso
    worst_time = []
    worst_input = worst_case(n)
    for _ in range(10):
        start = time.time()
        selection_sort(worst_input)
        end = time.time()
        worst_time.append(end - start)
    worst_times.append(np.mean(worst_time))

    # Caso promedio
    average_time = []
    average_input = average_case(n)
    for _ in range(10):
        start = time.time()
        selection_sort(average_input)
        end = time.time()
        average_time.append(end - start)
    average_times.append(np.mean(average_time))

# Graficar los tiempos de ejecución
plt.figure(figsize=(8,6))
plt.plot(sizes, best_times, label="Best case", color="green", linewidth=2)
plt.plot(sizes, worst_times, label="Worst case", color="blue", linewidth=2)
plt.plot(sizes, average_times, label="Average case", color="red", linewidth=2)
plt.xlabel("Tamaño del Arreglo (n)")
plt.ylabel("Tiempo de ejecución (s)")
plt.legend()
plt.grid(True)
plt.title("Comparación de Tiempos de Ejecución de Selection Sort")
plt.show()