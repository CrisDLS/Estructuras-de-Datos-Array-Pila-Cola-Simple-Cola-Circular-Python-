import random
import time
from Pilas.TDA_Pila_Generica import Pila


def probar_pila(etiqueta: str, datos: list):
    print(f"\n--- {etiqueta} ---")

    # ==========================================
    # 1. Medición: Creación y llenado inicial (Push masivo)
    # ==========================================
    inicio_creacion_ns = time.perf_counter_ns()
    mi_pila: Pila[int] = Pila()
    for item in datos:
        mi_pila.push(item)
    fin_creacion_ns = time.perf_counter_ns()

    ns_creacion = fin_creacion_ns - inicio_creacion_ns
    ms_creacion = ns_creacion / 1_000_000
    ticks_creacion = ns_creacion / 100

    # ==========================================
    # 2. Medición: Operaciones lógicas del TDA (sin prints)
    # ==========================================
    inicio_ops_ns = time.perf_counter_ns()

    tamano_inicial = mi_pila.size()
    vacio_resultado = mi_pila.is_empty()
    elemento_tope = mi_pila.peek()
    elemento_desapilado = mi_pila.pop()  # Retira el elemento superior
    tamano_final = mi_pila.size()

    fin_ops_ns = time.perf_counter_ns()

    ns_operaciones = fin_ops_ns - inicio_ops_ns
    ns_total = ns_creacion + ns_operaciones
    ms_total = ns_total / 1_000_000
    ticks_total = ns_total / 100

    # ==========================================
    # 3. Presentación de resultados en consola
    # ==========================================
    print(f"Elementos apilados: {datos}")
    print(f"Tamaño inicial: {tamano_inicial}")
    print(f"¿Pila vacía?: {vacio_resultado}")
    print(f"Elemento en el tope (peek): {elemento_tope}")
    print(f"Elemento retirado (pop): {elemento_desapilado}")
    print(f"Tamaño tras pop: {tamano_final}")

    print(
        f"\nTiempo de llenado/push: {ms_creacion:.6f} ms | {ticks_creacion:.0f} ticks"
    )
    print(
        f"Tiempo total (TDA):     {ms_total:.6f} ms | {ticks_total:.0f} ticks"
    )


def operaciones_pilas():
    # Calentamiento para estabilizar la caché L1/L2 del procesador
    pila_warmup: Pila[int] = Pila()
    pila_warmup.push(0)
    _ = pila_warmup.pop()

    # Casos de prueba solicitados: 5, 10, 15 y 20 elementos
    casos = {
        "5 elementos": random.sample(range(100), 5),
        "10 elementos": random.sample(range(100), 10),
        "15 elementos": random.sample(range(100), 15),
        "20 elementos": random.sample(range(100), 20),
    }

    for nombre, datos in casos.items():
        probar_pila(nombre, datos)


if __name__ == "__main__":
    operaciones_pilas()