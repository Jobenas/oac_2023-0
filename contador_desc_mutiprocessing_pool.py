import time
from multiprocessing import Pool

CUENTA = 50_000_000

num_proc = 4

def cuenta(n: int) -> None:
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    inputs = [CUENTA // num_proc] * num_proc

    p = Pool(processes=num_proc)
    res = p.map(cuenta, inputs)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo de cuenta descendente multiproceso con pool: {fin - inicio:0.2f} segundos")
