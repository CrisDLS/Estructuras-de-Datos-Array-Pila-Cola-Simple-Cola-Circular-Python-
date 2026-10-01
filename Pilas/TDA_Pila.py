class Pila:
    def __init__(self):
        self.elementos = []
          # Lista interna para guardar los datos
    def push(self, item):
        self.elementos.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.elementos.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.elementos[-1]
    def is_empty(self):
        return len(self.elementos) == 0

    def size(self):
        return len(self.elementos)
    def size(self):
        """Devuelve el número de elementos en la pila"""
        return len(self.elementos)
    def __str__(self):
            """Representación visual de la pila desde el tope hasta el fondo."""
            if self.is_empty():
                return "Pila vacía: []"
            formato = " -> ".join(str(e) for e in self.elementos)
            return f"[TOPE] {formato} [FONDO]"

# Probando la clase Pilas 
mi_pila = Pila()

print("¿La pila está vacía?", mi_pila.is_empty())

# Apilando los elementos
mi_pila.push("Plato 1 (Abajo)")
mi_pila.push("Plato 2 (Medio)")
mi_pila.push("Plato 3 (Arriba)")

print("Cantidad de platos en la pila:", mi_pila.size())
print("Plato en el tope:", mi_pila.peek())

# Desapilando 
print("\nRetirando el plato superior:", mi_pila.pop())
print("Nuevo plato en el tope:", mi_pila.peek())
print("Cantidad restante:", mi_pila.size())
    