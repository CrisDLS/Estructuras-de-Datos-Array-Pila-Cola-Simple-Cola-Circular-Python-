"""
ESTRUCTURA DE DATOS: Cola (Queue)
PRINCIPIO FUNDAMENTAL: FIFO (First-In, First-Out / Primero en entrar, primero en salir)

ANALOGÍA DEL MUNDO REAL:
    Una fila en la caja de un banco o una cola de impresión. 
    Los nuevos elementos llegan al final de la fila y solo se atiende 
    o despacha al que está en el frente.

OPERACIONES PRINCIPALES:
    1. Crear: Inicializar la estructura vacía.
    2. Encolar (Enqueue): Insertar un elemento al final de la cola.
    3. Desencolar (Dequeue): Eliminar y retornar el elemento del frente.
    4. Frente (Peek / Front): Consultar el elemento del frente sin retirarlo.
    5. IsEmpty: Verificar si la cola está vacía.
    6. Buscar: Localizar la posición de un elemento en espera.
"""


class Cola:
    """Implementación del TDA Cola basada en listas nativas de Python."""

    def __init__(self):
        """1. CREAR: Inicializa la cola vacía."""
        self.elementos = []

    # -------------------------------------------------------------
    # 2. ENCOLAR / INSERTAR
    # -------------------------------------------------------------
    def enqueue(self, valor):
        """
        Agrega un elemento al final de la cola.
        Equivalente a formarse en la fila.
        Complejidad temporal: O(1) amortizado.
        """
        self.elementos.append(valor)

    # -------------------------------------------------------------
    # 3. DESENCOLAR / ELIMINAR
    # -------------------------------------------------------------
    def dequeue(self):
        """
        Elimina y retorna el elemento en el frente de la cola (índice 0).
        Respeta la regla FIFO (el primero que llegó es el primero en salir).
        Lanza IndexError si la cola está vacía.
        Complejidad temporal: O(n) al desplazar los elementos restantes.
        """
        if self.is_empty():
            raise IndexError("La cola está vacía, no se puede desencolar.")
        return self.elementos.pop(0)

    # -------------------------------------------------------------
    # 4. CONSULTAR FRENTE (PEEK)
    # -------------------------------------------------------------
    def peek(self):
        """
        Retorna el elemento al frente de la cola sin eliminarlo.
        Permite saber quién es el próximo en ser atendido.
        """
        if self.is_empty():
            raise IndexError("La cola está vacía.")
        return self.elementos[0]

    # -------------------------------------------------------------
    # 5. ESTADO Y TAMAÑO
    # -------------------------------------------------------------
    def is_empty(self):
        """Verifica si la cola no contiene elementos."""
        return len(self.elementos) == 0

    def tamano(self):
        """Retorna la cantidad total de elementos formados."""
        return len(self.elementos)

    # -------------------------------------------------------------
    # 6. BUSCAR
    # -------------------------------------------------------------
    def buscar(self, valor):
        """
        Localiza la posición de turno de un elemento en la cola.
        Retorna el turno (0 = frente) o -1 si no está en la cola. O(n).
        """
        for indice, elemento in enumerate(self.elementos):
            if elemento == valor:
                return indice
        return -1

    def __str__(self):
        """Representación visual de la cola desde el frente hasta el final."""
        if self.is_empty():
            return "Cola vacía: []"
        formato = " -> ".join(str(e) for e in self.elementos)
        return f"[FRENTE] {formato} [FINAL]"


# =====================================================================
# CASO DE USO REAL: SIMULACIÓN DE ATENCIÓN DE CLIENTES EN UN BANCO
# =====================================================================

def demostracion_caso_real():
    print("=== SISTEMA DE TURNOS BANCARIOS (TDA COLA - FIFO) ===\n")

    # 1. Crear la cola
    fila_banco = Cola()
    print(f"¿La fila está vacía al abrir la sucursal?: {fila_banco.is_empty()}")

    # 2. Llegan clientes a formarse (Enqueue)
    print("\n--- Clientes llegando a ventanilla ---")
    fila_banco.enqueue("Cliente 101 (Ana)")
    fila_banco.enqueue("Cliente 102 (Beto)")
    fila_banco.enqueue("Cliente 103 (Carlos)")
    print(f"Estado de la fila: {fila_banco}")
    print(f"Total de personas en espera: {fila_banco.tamano()}")

    # 3. Consultar quién es el siguiente turno sin sacarlo (Peek)
    siguiente = fila_banco.peek()
    print(f"\n[Peek] El próximo en ser llamado a ventanilla es: {siguiente}")

    # 4. Buscar la posición de un cliente en la fila (Buscar)
    cliente_consulta = "Cliente 103 (Carlos)"
    posicion = fila_banco.buscar(cliente_consulta)
    if posicion != -1:
        print(f"[Buscar] '{cliente_consulta}' está en la posición/turno: {posicion} de la fila.")

    # 5. La ventanilla atiende por orden de llegada (Dequeue)
    print("\n--- Ventanilla abierta: Despachando turnos ---")
    atendido1 = fila_banco.dequeue()
    print(f"Atendiendo a: {atendido1}")
    print(f"Fila restante: {fila_banco}")

    atendido2 = fila_banco.dequeue()
    print(f"Atendiendo a: {atendido2}")
    print(f"Fila restante: {fila_banco}")

    # 6. Verificación de vaciado y control de excepciones
    print("\nAtendiendo al último cliente...")
    fila_banco.dequeue()
    print(f"¿Queda alguien en la fila?: {fila_banco.is_empty()}")

    print("\nIntentando atender con la fila vacía:")
    try:
        fila_banco.dequeue()
    except IndexError as error:
        print(f"Excepción capturada correctamente: {error}")


if __name__ == "__main__":
    demostracion_caso_real()