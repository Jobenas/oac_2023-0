import time

def suma_sin_io() -> int:
    a = 4
    b = 5

    return a + b


def suma_con_io() -> int:
    a = int(input("ingrese numero a: "))
    b = int(input("ingrese numero b: "))

    return a + b


def suma_con_parametros(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    inicio_sin_io = time.perf_counter()
    res_sin_io = suma_sin_io()
    fin_sin_io = time.perf_counter()

    inicio_con_io = time.perf_counter()
    res_con_io = suma_con_io()
    fin_con_io = time.perf_counter()

    a_parametro = int(input("ingrese el numero a: "))
    b_parametro = int(input("ingrese el numero b: "))

    inicio_con_parametros = time.perf_counter()
    res_con_parametros = suma_con_parametros(a_parametro, b_parametro)
    fin_con_parametros = time.perf_counter()

    print(f"suma sin io {res_sin_io}")
    print(f"suma con io {res_con_io}")
    print(f"suma con parametros {res_con_parametros}")

    print(f"Tiempo de ejecución sin I/O: {fin_sin_io - inicio_sin_io} segundos")
    print(f"Tiempo de ejecución con I/O: {fin_con_io - inicio_con_io} segundos")
    print(f"Tiempo de ejecución con parametros: {fin_con_parametros - inicio_con_parametros} segundos")
