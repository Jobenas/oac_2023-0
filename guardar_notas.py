import random
import time


def generar_notas(rango: int) -> str:
    codigo_base = 20230000
    contenido = "codigo,pa1,pa2,pa3,pa4,pb1,pb2,pb3,pb4,pb5,e1,e2\n"
    for i in range(1,rango + 1):
        pa = [random.randint(0,20) for _ in range(4)]
        pb = [random.randint(0,20) for _ in range(5)]
        e1 = random.randint(0,20)
        e2 = random.randint(0,20)
        linea = f"{codigo_base + i},{pa[0]},{pa[1]},{pa[2]},{pa[3]},{pb[0]},{pb[1]},{pb[2]},{pb[3]},{pb[4]},{e1},{e2}\n"
        contenido += linea
    
    return contenido


if __name__ == '__main__':
    inicio_total = time.perf_counter()
    inicio_cpu = time.perf_counter()
    contenido = generar_notas(40)
    fin_cpu = time.perf_counter()

    inicio_io = time.perf_counter()
    with open("notas.csv", "w+") as archivo:
        archivo.write(contenido)
    fin_io = time.perf_counter()
    fin_total = time.perf_counter()

    print(f"Tiempo de ejecución CPU: {fin_cpu - inicio_cpu} segundos")
    print(f"Tiempo de ejecución I/O: {fin_io - inicio_io} segundos")
    print(f"Tiempo de ejecución total: {fin_total - inicio_total} segundos")

    p_cpu = ((fin_cpu - inicio_cpu) / (fin_total - inicio_total)) * 100
    p_io = ((fin_io - inicio_io) / (fin_total - inicio_total)) * 100

    print("Porcentaje de tiempo de CPU: {:.2f}%".format(p_cpu))
    print("Porcentaje de tiempo de I/O: {:.2f}%".format(p_io))
