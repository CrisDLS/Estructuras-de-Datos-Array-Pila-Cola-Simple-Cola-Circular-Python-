"""
ESTRUCTURA DE DATOS: Array Unidimensional (Vector) Genérico
CONCEPTO CLAVE: Colección lineal de elementos de tipo T indexados desde 0 hasta (tamaño - 1).
"""

from typing import Generic, Iterable, List, Optional, TypeVar
import time

# 1. Definición de la variable de tipo genérico
T = TypeVar("T")


# 2. La clase hereda de Generic[T]
class Arreglo(Generic[T]):
    """Implementación del TDA Arreglo Unidimensional Genérico basado en listas de Python."""

    def __init__(self, elementos_iniciales: Optional[Iterable[T]] = None) -> None:
        """1. CREAR: Inicializa la estructura tipada para elementos de tipo T."""
        if elementos_iniciales is None:
            self.elementos: List[T] = []
        else:
            self.elementos: List[T] = list(elementos_iniciales)

    # -------------------------------------------------------------
    # 2. AGREGAR / INSERTAR
    # -------------------------------------------------------------
    def agregar(self, valor: T) -> None:
        """Agrega un elemento de tipo T al final del arreglo. O(1) amortizado."""
        self.elementos.append(valor)

    def insertar(self, indice: int, valor: T) -> None:
        """Inserta un valor de tipo T en una posición específica. O(n)."""
        if 0 <= indice <= len(self.elementos):
            self.elementos.insert(indice, valor)
        else:
            raise IndexError("Índice fuera del rango permitido.")

    # -------------------------------------------------------------
    # 3. ELIMINAR
    # -------------------------------------------------------------
    def eliminar_por_indice(self, indice: int) -> T:
        """Elimina y retorna el dato de tipo T en el índice indicado. O(n)."""
        if self.is_empty():
            raise IndexError("El arreglo está vacío.")
        if not (0 <= indice < len(self.elementos)):
            raise IndexError("Índice fuera de límites.")
        return self.elementos.pop(indice)

    # -------------------------------------------------------------
    # 4. BUSCAR Y ACCEDER
    # -------------------------------------------------------------
    def obtener(self, indice: int) -> T:
        """Acceso directo por índice numérico retornando un dato tipo T. O(1)."""
        if not (0 <= indice < len(self.elementos)):
            raise IndexError("Índice fuera de límites.")
        return self.elementos[indice]

    def buscar(self, valor: T) -> int:
        """Busca secuencialmente un valor de tipo T y devuelve su índice. O(n)."""
        for i in range(len(self.elementos)):
            if self.elementos[i] == valor:
                return i
        return "No encontrado"  # Retorna un mensaje si no se encuentra el valor

    # -------------------------------------------------------------
    # 5. ORDENAR
    # -------------------------------------------------------------
    def ordenar(self, descendente: bool = False) -> None:
        """Ordena los elementos de menor a mayor (o viceversa). O(n log n)."""
        self.elementos.sort(reverse=descendente)

    # -------------------------------------------------------------
    # MÉTODOS AUXILIARES
    # -------------------------------------------------------------
    def tamano(self) -> int:
        """Retorna la cantidad total de elementos."""
        return len(self.elementos)

    def is_empty(self) -> bool:
        """Verifica si la estructura no contiene datos."""
        return len(self.elementos) == 0

    def __str__(self) -> str:
        """Representación visual del vector."""
        return str(self.elementos)


# =====================================================================
# EJEMPLO EN LA VIDA REAL: CONTROL DE CALIFICACIONES DE UN GRUPO
# =====================================================================

def demostracion_caso_real() -> None:
    print("=== GESTIÓN DE CALIFICACIONES ESCOLARES (TDA ARREGLO GENÉRICO) ===\n")
    inicio = time.perf_counter()

    # Instanciamos indicando explícitamente el tipo genérico [float]
    calificaciones: Arreglo[float] = Arreglo([8.5, 9.0, 7.2, 10.0, 6.5])
    print(f"Vector inicial creado: {calificaciones}")
    print(f"Total de alumnos (tamaño): {calificaciones.tamano()}")

    # Acceso instantáneo O(1)
    primer_alumno: float = calificaciones.obtener(0)
    ultimo_alumno: float = calificaciones.obtener(calificaciones.tamano() - 1)
    print(f"\n[Acceso O(1)] Primer índice (0): {primer_alumno}")
    print(f"[Acceso O(1)] Último índice ({calificaciones.tamano() - 1}): {ultimo_alumno}")

    # Agregar nuevo dato de tipo float
    calificaciones.agregar(9.5)
    print(f"\n[Agregar] Alumno nuevo añadido al final: {calificaciones}")

    # Buscar un elemento O(n)
    nota_a_buscar = 10.0
    posicion = calificaciones.buscar(nota_a_buscar)
    if posicion != -1:
        print(f"[Buscar] La calificación {nota_a_buscar} se encuentra en el índice {posicion}.")

    # Ordenar el arreglo
    print("\n[Ordenar] Ordenando calificaciones de mayor a menor...")
    calificaciones.ordenar(descendente=True)
    print(f"Vector ordenado: {calificaciones}")

    # Eliminar un elemento
    expulsado: float = calificaciones.eliminar_por_indice(0)
    print(f"\n[Eliminar] Se dio de baja la nota {expulsado}.")
    print(f"Estado final del arreglo: {calificaciones}")

    # Medición de tiempo de ejecución
    fin = time.perf_counter()
    tiempo_total_segundos = fin - inicio
    tiempo_milisegundos = tiempo_total_segundos * 1000

    print(f"\nTiempo total de ejecución: {tiempo_total_segundos:.6f} segundos")
    print(f"Tiempo en milisegundos: {tiempo_milisegundos:.3f} ms")

if __name__ == "__main__":
    demostracion_caso_real()