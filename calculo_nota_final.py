import time

def calcula_nota(linea: str) -> list[str, float]:
    notas = linea.split(",")
    pa = [notas[1], notas[2], notas[3], notas[4]]
    pb = [notas[5], notas[6], notas[7], notas[8], notas[9]]
    pa.remove(min(pa))
    pa = [int(x) for x in pa]
    pb = [int(x) for x in pb]
    e1 = int(notas[10])
    e2 = int(notas[11])
    pa_prom = sum(pa) / len(pa)
    pb_prom = sum(pb) / len(pb)

    nota_final = (3 * pa_prom + 3 * pb_prom + 2 * e1 + 2 * e2) / 10.0

    return [notas[0], nota_final]


def main_linea_por_linea():
    idx = 0
    tiempos_io = list()
    tiempos_cpu = list()
    tiempos_totales = list()
    with open("notas.csv", "r") as f:
        while True:
            inicio_total = time.perf_counter()
            inicio_io = time.perf_counter()
            linea = f.readline()
            fin_io = time.perf_counter()
            tiempos_io.append(fin_io - inicio_io)
            if not linea:
                break
            if idx == 0:
                idx = idx + 1
                continue
            inicio_cpu = time.perf_counter()
            res = calcula_nota(linea)
            fin_cpu = time.perf_counter()
            tiempos_cpu.append(fin_cpu - inicio_cpu)
            fin_total = time.perf_counter()
            print(res)
            tiempos_totales.append(fin_total - inicio_total)

    prom_tiempo_io = sum(tiempos_io) / len(tiempos_io)
    prom_tiempo_cpu = sum(tiempos_cpu) / len(tiempos_cpu)
    prom_tiempo_total = sum(tiempos_totales) / len(tiempos_totales)

    print(f"Tiempo promedio de I/O: {prom_tiempo_io} segundos")
    print(f"Tiempo promedio de CPU: {prom_tiempo_cpu} segundos")
    print(f"Tiempo promedio total: {prom_tiempo_total} segundos")


def main_una_sola_lectura():
    idx = 0
    tiempos_io = list()
    tiempos_cpu = list()
    tiempos_totales = list()
    with open("notas.csv", 'r') as f:
        inicio_io = time.perf_counter()
        contenido = f.read()
        fin_io = time.perf_counter()
        tiempos_io.append(fin_io - inicio_io)
    
    lineas = contenido.split("\n")

    for linea in lineas:
        if idx == 0:
            idx = idx + 1
            continue
        if linea == "":
            continue
        inicio_cpu = time.perf_counter()
        res = calcula_nota(linea)
        fin_cpu = time.perf_counter()
        tiempos_cpu.append(fin_cpu - inicio_cpu)
        print(res)

    prom_tiempo_io = sum(tiempos_io) / len(tiempos_io)
    prom_tiempo_cpu = sum(tiempos_cpu) / len(tiempos_cpu)

    print(f"Tiempo promedio de I/O: {prom_tiempo_io} segundos")
    print(f"Tiempo promedio de CPU: {prom_tiempo_cpu} segundos")

if __name__ == '__main__':
    # main_linea_por_linea()
    main_una_sola_lectura()