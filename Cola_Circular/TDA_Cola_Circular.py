"""
ESTRUCTURA DE DATOS: Cola Circular (Circular Queue / Ring Buffer)
PRINCIPIO FUNDAMENTAL: FIFO (First-In, First-Out) sobre un arreglo de tamaño fijo.

CONCEPTO CLAVE:
    A diferencia de una cola lineal sobre arreglo donde al desencolar queda
    espacio inutilizable al inicio, en una cola circular el último elemento
    se conecta conceptualmente con el primero mediante aritmética modular:
        posicion_siguiente = (posicion_actual + 1) % capacidad

VENTAJAS TÉCNICAS:
    - Evita el desperdicio de memoria y el desplazamiento de datos O(n).
    - Inserción (enqueue) y eliminación (dequeue) se ejecutan en O(1) estricto.
    - Uso eficiente de memoria estática (ideal para búferes de streaming,
      audio en tiempo real y sistemas embebidos).

OPERACIONES DEL TDA:
    1. enqueue(valor): Inserta al final del recorrido circular.
    2. dequeue(): Extrae del frente del recorrido circular.
    3. peek(): Consulta el elemento del frente sin extraerlo.
    4. is_empty(): Determina si la cola carece de elementos.
    5. is_full(): Determina si la cola alcanzó su límite de capacidad.
"""

from typing import Generic, List, Optional, TypeVar

# Definición del parámetro de tipo genérico
T = TypeVar("T")


class ColaCircular(Generic[T]):
    """Implementación genérica formal de una Cola Circular de capacidad fija."""

    def __init__(self, capacidad: int) -> None:
        """
        Inicializa la cola circular con un tamaño máximo establecido.
        
        :param capacidad: Número máximo de elementos que puede almacenar.
        """
        if capacidad <= 0:
            raise ValueError("La capacidad de la cola debe ser mayor a 0.")

        self._capacidad: int = capacidad
        # Se reserva memoria contigua inicializada con None
        self._elementos: List[Optional[T]] = [None] * capacidad
        self._frente: int = 0
        self._final: int = 0
        self._tamano_actual: int = 0

    def enqueue(self, valor: T) -> None:
        """
        Inserta un elemento en la posición final actual y desplaza el puntero
        usando aritmética modular.
        
        Complejidad temporal: O(1)
        :raises OverflowError: Si la cola está llena.
        """
        if self.is_full():
            raise OverflowError(
                f"Cola llena (Overflow). Capacidad máxima alcanzada: {self._capacidad} elementos."
            )

        self._elementos[self._final] = valor
        # Avance circular del índice final
        self._final = (self._final + 1) % self._capacidad
        self._tamano_actual += 1

    def dequeue(self) -> T:
        """
        Extrae y retorna el elemento en el frente de la cola, liberando su posición.
        
        Complejidad temporal: O(1)
        :raises IndexError: Si la cola no contiene datos.
        """
        if self.is_empty():
            raise IndexError("Cola vacía (Underflow). No hay elementos para desencolar.")

        dato_extraido = self._elementos[self._frente]
        # Limpieza de referencia para recolección de basura
        self._elementos[self._frente] = None
        # Avance circular del índice frente
        self._frente = (self._frente + 1) % self._capacidad
        self._tamano_actual -= 1

        # dato_extraido no es None debido a la verificación previa is_empty
        return dato_extraido  # type: ignore[return-value]

    def peek(self) -> T:
        """
        Consulta el valor situado en el frente sin modificar los índices.
        
        Complejidad temporal: O(1)
        :raises IndexError: Si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("La cola circular está vacía.")
        return self._elementos[self._frente]  # type: ignore[return-value]

    def is_empty(self) -> bool:
        """Verifica si la cola circular no tiene elementos almacenados."""
        return self._tamano_actual == 0

    def is_full(self) -> bool:
        """Verifica si la cola circular ha ocupado todas sus posiciones disponibles."""
        return self._tamano_actual == self._capacidad

    def tamano(self) -> int:
        """Retorna el número de elementos actualmente formados."""
        return self._tamano_actual

    def capacidad(self) -> int:
        """Retorna la capacidad total asignada a la estructura."""
        return self._capacidad

    def __str__(self) -> str:
        """
        Representación en cadena mostrando el orden lógico FIFO
        desde el frente hasta el final.
        """
        if self.is_empty():
            return "ColaCircular: [] (Vacía)"

        datos_ordenados: List[str] = []
        indice = self._frente
        for _ in range(self._tamano_actual):
            datos_ordenados.append(str(self._elementos[indice]))
            indice = (indice + 1) % self._capacidad

        return f"[FRENTE] {' -> '.join(datos_ordenados)} [FINAL] (Ocupación: {self._tamano_actual}/{self._capacidad})"


# =====================================================================
# CASO DE USO REAL: BÚFER CIRCULAR DE TRANSMISIÓN DE AUDIO (STREAMING)
# =====================================================================

def demostracion_caso_real() -> None:
    print("=== SIMULADOR DE BÚFER CIRCULAR DE AUDIO (TDA COLA CIRCULAR) ===\n")

    # 1. Creamos un búfer circular tipado estrictamente a 'str' con capacidad fija de 4 paquetes
    buffer_audio: ColaCircular[str] = ColaCircular(capacidad=4)
    print(f"Capacidad del búfer reservada: {buffer_audio.capacidad()} paquetes.")
    print(f"¿Búfer vacío?: {buffer_audio.is_empty()}\n")

    # 2. Llegan los primeros paquetes de audio de la red
    print("--- Recibiendo paquetes de audio por la red ---")
    buffer_audio.enqueue("Frame_Audio_01")
    buffer_audio.enqueue("Frame_Audio_02")
    buffer_audio.enqueue("Frame_Audio_03")
    print(buffer_audio)

    # 3. La tarjeta de sonido reproduce (desencola) un paquete
    print("\n--- Tarjeta de sonido reproduciendo en tiempo real ---")
    reproducido = buffer_audio.dequeue()
    print(f"[REPRODUCIENDO]: {reproducido}")
    print(f"Estado tras reproducción: {buffer_audio}")

    # 4. Llegan más paquetes aprovechando el espacio circular reutilizado
    print("\n--- Llegada de nuevos paquetes (Reutilización de índices) ---")
    buffer_audio.enqueue("Frame_Audio_04")
    buffer_audio.enqueue("Frame_Audio_05")
    print(buffer_audio)
    print(f"¿Búfer completamente lleno?: {buffer_audio.is_full()}")

    # 5. Intentar saturar el búfer (Desbordamiento controlado)
    print("\n--- Intentando sobrecargar el búfer sin procesar ---")
    try:
        buffer_audio.enqueue("Frame_Audio_06_Perdido")
    except OverflowError as error:
        print(f"Aviso capturado correctamente: {error}")

    # 6. Vaciar el búfer conforme concluye la pista
    print("\n--- Consumiendo todos los paquetes pendientes ---")
    while not buffer_audio.is_empty():
        print(f"Reproduciendo: {buffer_audio.dequeue()}")

    print(f"\nEstado final del búfer: {buffer_audio}")
    print(f"¿Búfer vacío?: {buffer_audio.is_empty()}")


if __name__ == "__main__":
    demostracion_caso_real()