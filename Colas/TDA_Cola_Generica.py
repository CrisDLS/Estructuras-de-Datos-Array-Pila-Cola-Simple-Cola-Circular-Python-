from typing import Generic, List, TypeVar, Optional

# 1. Se declara la variable de tipo genérico
T = TypeVar("T")


# 2. La clase hereda de Generic[T]
class Cola(Generic[T]):
    """Implementación formal del TDA Cola usando Clases Genéricas en Python."""

    def __init__(self, capacidad: int) -> None:
        """Inicializa la cola con una lista que solo admitirá elementos de tipo T."""
        if capacidad <= 0:
            raise ValueError("La capacidad de la cola debe ser mayor a 0.")
        
        self.capacidad: int = capacidad
        # Se reserva memoria contigua inicializada con None
        self.elementos: List[Optional[T]] = [None] * capacidad
        self.frente: int = 0
        self.final: int = 0

    def enqueue(self, valor: T) -> None:
        """Recibe estrictamente un valor del tipo T definido."""
        if self.final == self.capacidad:
            raise OverflowError("La cola está llena, no se puede encolar (desbordamiento falso).")
        self.elementos[self.final] = valor
        self.final += 1

    def dequeue(self) -> T:
        """Retorna un elemento del tipo T."""
        if self.frente == self.final:
            raise IndexError("La cola está vacía, no se puede desencolar.")
        valor = self.elementos[self.frente]
        self.elementos[self.frente] = None  
        self.frente += 1

        # REINICIO SI QUEDA TOTALMENTE VACÍA:
        if self.frente == self.final:
            self.frente = 0
            self.final = 0

        return valor

    def peek(self) -> T:
        """Consulta el frente retornando el tipo T sin eliminarlo."""
        if self.is_empty():
            raise IndexError("La cola está vacía.")
        return self.elementos[self.frente]

    def is_empty(self) -> bool:
        return self.frente == self.final

    def tamano(self) -> int:
        return self.final - self.frente

    def buscar(self, valor: T) -> int:
        """Busca un valor de tipo T y retorna su índice o -1."""
        for indice, elemento in enumerate(self.elementos[self.frente:self.final]):
            if elemento == valor:
                return indice + self.frente
        return -1

    def __str__(self) -> str:
        if self.is_empty():
            return "Cola vacía: []"
        formato = " -> ".join(str(e) for e in self.elementos[self.frente:self.final] if e is not None)
        return f"[FRENTE] {formato} [FINAL]"

def ejemplo_cola():
    fila_banco: Cola[str] = Cola[str](3)
    
    # 1. Se llena por completo
    fila_banco.enqueue("Alice")
    fila_banco.enqueue("Bob")
    fila_banco.enqueue("Charlie")
    print("Cola llena:", fila_banco)
    print("Arreglo real en memoria:", fila_banco.elementos)

    # 2. Se libera un espacio del frente
    print(f"\nDesencolando: {fila_banco.dequeue()}")
    print("Cola después de dequeue:", fila_banco)
    print("Arreglo real en memoria:", fila_banco.elementos)  # Verás: [None, 'Bob', 'Charlie']

    # 3. Demostración del desperdicio de memoria / falso desbordamiento
    try:
        print("\nIntentando encolar a 'David'...")
        fila_banco.enqueue("David")
    except OverflowError as e:
        print(f"Error capturado con éxito: {e}")

if __name__ == "__main__":
    ejemplo_cola()