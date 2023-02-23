import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count

M = 5000
N = 5000


def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(y)):
        suma += x[i] * y[i]

    return suma


def main(mat_M, vector_A, pool_size):
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=pool_size)
    resultados = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()

    return resultados


if __name__ == '__main__':

    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(M, ))

    pool_sizes = [2, 4, 8, 16, 32]

    tiempos = list()

    for pool_size in pool_sizes:
        print(f"Evaluando pool size: {pool_size}")
        size_times = list()
        for i in range(10):
            print(f"Iteracion: {i + 1}")
            inicio = time.perf_counter()
            main(mat_M, vector_A, pool_size)
            fin = time.perf_counter()
            size_times.append(fin - inicio)
        tiempo_prom = sum(size_times) / len(size_times)
        tiempos.append(tiempo_prom)

    print("Tiempos de ejecucion para diferentes tamaños de pool:")
    for i in range(len(pool_sizes)):
        print("Pool size: ", pool_sizes[i], "Tiempo: ", tiempos[i])


