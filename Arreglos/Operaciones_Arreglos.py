import random
import time
from Arreglos.TDA_Array_Generica import Arreglo


def probar_arreglo(etiqueta: str, datos: list):
    print(f"\n--- {etiqueta} ---")

    # ==========================================
    # 1. Medición: Solo creación
    # ==========================================
    inicio_creacion_ns = time.perf_counter_ns()
    mi_arreglo = Arreglo(datos)
    fin_creacion_ns = time.perf_counter_ns()

    ns_creacion = fin_creacion_ns - inicio_creacion_ns
    ms_creacion = ns_creacion / 1_000_000
    ticks_creacion = ns_creacion / 100

    # ==========================================
    # 2. Medición: Operaciones lógicas (sin prints)
    # ==========================================
    inicio_ops_ns = time.perf_counter_ns()

    tamano_resultado = mi_arreglo.tamano()
    vacio_resultado = mi_arreglo.is_empty()
    busqueda_10 = mi_arreglo.buscar(10)
    busqueda_55 = mi_arreglo.buscar(55)
    mi_arreglo.ordenar(descendente=True)
    elemento_indice_4 = mi_arreglo.obtener(4) if tamano_resultado > 4 else None

    fin_ops_ns = time.perf_counter_ns()

    # Tiempo de operaciones + tiempo de creación = Tiempo Total
    ns_operaciones = fin_ops_ns - inicio_ops_ns
    ns_total = ns_creacion + ns_operaciones
    ms_total = ns_total / 1_000_000
    ticks_total = ns_total / 100

    # ==========================================
    # 3. Muestra de resultados en consola
    # ==========================================
    print(f"Tamaño: {tamano_resultado}")
    print(f"Contenido ordenado: {mi_arreglo}")
    print(f"¿Vacío?: {vacio_resultado}")
    print(f"Buscar el número 10: {busqueda_10}")
    print(f"Buscar el número 55: {busqueda_55}")
    if elemento_indice_4 is not None:
        print(f"Elemento en índice 4: {elemento_indice_4}")

    print(
        f"\nTiempo de creación:  {ms_creacion:.6f} ms | {ticks_creacion:.0f} ticks"
    )
    print(
        f"Tiempo total (TDA):  {ms_total:.6f} ms | {ticks_total:.0f} ticks"
    )


def operaciones_arreglos():
    # Calentamiento para estabilizar caché de CPU
    _ = Arreglo([0])

    casos = {
        "5 elementos": list(random.sample(range(100), 5)),
        "10 elementos": list(random.sample(range(100), 10)),
        "15 elementos": list(random.sample(range(100), 15)),
        "20 elementos": list(random.sample(range(100), 20)),
    }

    for nombre, datos in casos.items():
        probar_arreglo(nombre, datos)


if __name__ == "__main__":
    operaciones_arreglos()