from typing import TypeVar, Generic, List

# Definimos una variable de tipo genérico (T)
T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self) -> None:
        self.elementos: List[T] = []  # Lista interna tipada con T
          
    def push(self, item: T) -> None:
        """Agrega un elemento a la pila"""
        self.elementos.append(item)
        
    def pop(self) -> T:
        """Retira y devuelve el elemento del tope"""
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.elementos.pop()
        
    def peek(self) -> T:
        """Devuelve el elemento del tope sin retirarlo"""
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.elementos[-1]
        
    def is_empty(self) -> bool:
        """Verifica si la pila está vacía"""
        return len(self.elementos) == 0

    def size(self) -> int:
        """Devuelve el número de elementos en la pila"""
        return len(self.elementos)


# --- Probando la clase Pila Genérica ---
if __name__ == "__main__":
    # Pila especializada en Cadenas de Texto (str)
    mi_pila_platos: Pila[str] = Pila()

    print("¿La pila está vacía?", mi_pila_platos.is_empty())

    # Apilando elementos de tipo str
    mi_pila_platos.push("Plato 1 (Abajo)")
    mi_pila_platos.push("Plato 2 (Medio)")
    mi_pila_platos.push("Plato 3 (Arriba)")

    print("Cantidad de platos en la pila:", mi_pila_platos.size())
    print("Plato en el tope:", mi_pila_platos.peek())

    # Desapilando 
    print("\nRetirando el plato superior:", mi_pila_platos.pop())
    print("Nuevo plato en el tope:", mi_pila_platos.peek())
    print("Cantidad restante:", mi_pila_platos.size())
    
    print("-" * 30)
    
    # Ejemplo con otra pila especializada en Enteros (int)
    mi_pila_numeros: Pila[int] = Pila()
    mi_pila_numeros.push(10)
    mi_pila_numeros.push(20)
    print("Tope de la pila numérica:", mi_pila_numeros.peek())