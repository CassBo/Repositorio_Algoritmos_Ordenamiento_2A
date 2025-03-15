import time
import random
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [8, 4, 7, 3, 5, 1, 9, 2]
print("Lista original:", arr)
merge_sort(arr)
print("Lista ordenada:", arr)

def medir_tiempo(n, repeticiones = 10):
    tiempos = []
    for _ in range(repeticiones):
        arr = [random.randint(0, 10000) for _ in range(n)]
        start_time = time.perf_counter()
        merge_sort(arr)
        end_time = time.perf_counter()
        tiempos.append(end_time - start_time)

    # Promedio de los tiempos
    return sum(tiempos) / len(tiempos)

tamaños = list(range(0, 10001, 1000))
tiempos = [medir_tiempo(n) for n in tamaños]

plt.plot(tamaños, tiempos, marker='o', linestyle='-', color='b', label="Merge Sort")
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de Merge Sort')
plt.legend()
plt.grid()
plt.show()

def time_merge_sort(arr):
  start = time.perf_counter()
  merge_sort(arr)
  return time.perf_counter() - start

sizes = list(range(0, 10001, 1000))
best_times = []
worst_times = []
average_times = []

for size in sizes:
  best_case = list(range(size))
  worst_case = list(range(size, 0, -1))
  average_case = sum(time_merge_sort(random.sample(range(size), size)) for _ in range(5)) / 5

  best_times.append(time_merge_sort(best_case))
  worst_times.append(time_merge_sort(worst_case))
  average_times.append(average_case)

#plt.plot(sizes, best_times, marker='o', linestyle='-', label='Mejor caso', color='g')
#plt.plot(sizes, worst_times, marker='o', linestyle='-', label='Peor caso', color='r')
plt.plot(sizes, average_times, marker='o', linestyle='-', label='Caso promedio', color='b')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo (s)')
plt.legend()
plt.title('Complejidad de Merge Sort')
plt.grid()
plt.show()