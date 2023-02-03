from hola_archivo import func
import time


if __name__ == '__main__':
    inicio = time.perf_counter()
    print(func(1, 2))
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio} segundos")