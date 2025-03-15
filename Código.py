import matplotlib.pyplot as plt
import numpy as np
import time

# Función de Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Función para medir el tiempo de ejecución
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Medir en milisegundos

# Generar listas para los diferentes casos
n_values = np.logspace(1, 4, num=10, dtype=int)  # Generar valores de n en progresión geométrica

best_case_times = []
worst_case_times = []
average_case_times = []

# Mejor caso: lista ya ordenada
for n in n_values:
    total_time = 0
    for _ in range(10):  # Ejecutar 10 veces
        best_case = list(range(n))  # Lista ordenada
        total_time += measure_time(insertion_sort, best_case)
    best_case_times.append(total_time / 10)  # Promediar el tiempo

# Peor caso: lista ordenada en orden inverso
for n in n_values:
    total_time = 0
    for _ in range(10):  # Ejecutar 10 veces
        worst_case = list(range(n, 0, -1))  # Lista ordenada inversamente
        total_time += measure_time(insertion_sort, worst_case)
    worst_case_times.append(total_time / 10)  # Promediar el tiempo

# Caso promedio: lista aleatoria
for n in n_values:
    total_time = 0
    for _ in range(10):  # Ejecutar 10 veces
        average_case = np.random.randint(0, 10000, n).tolist()  # Aumentar el rango de números aleatorios
        total_time += measure_time(insertion_sort, average_case)
    average_case_times.append(total_time / 10)  # Promediar el tiempo

# Imprimir los tiempos de ejecución
print("Tiempos de ejecución (en milisegundos):")
print("Tamaño de entrada (n) | Mejor Caso | Peor Caso | Caso Promedio")
for i in range(len(n_values)):
    print(f"{n_values[i]:<20} | {best_case_times[i]:<12.6f} | {worst_case_times[i]:<10.6f} | {average_case_times[i]:<12.6f}")

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(n_values, best_case_times, label='Mejor Caso O(n)', color='green')
plt.plot(n_values, worst_case_times, label='Peor Caso O(n^2)', color='red')
plt.plot(n_values, average_case_times, label='Caso Promedio O(n^2)', color='blue')

# Configuraciones de la gráfica
plt.title('Tiempo de Ejecución de Insertion Sort')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de Ejecución (milisegundos)')
plt.legend()
plt.grid()
plt.ylim(0, 10)  # Ajustar el límite del eje y para mejor visualización
plt.xlim(0, 5000)  # Ajustar el límite del eje x para mejor visualización
plt.show()
