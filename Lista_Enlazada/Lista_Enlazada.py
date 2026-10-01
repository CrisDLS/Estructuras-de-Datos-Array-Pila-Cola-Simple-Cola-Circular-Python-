class Nodo:
    def __init__(self, dato):
        self.dato = dato          # El valor que vamos a  guardar 
        self.siguiente = None     # La dirección del siguiente nodo en la cadena
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # El primer nodo de la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        # Si no está vacía, se busca el último nodo
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        # Conecta con el último nodo con el nuevo nodo
        actual.siguiente = nuevo_nodo
    def mostrar(self):
        actual = self.cabeza
        elementos = []
        
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
            
        # Imprimime en formato visual de cadena
        print(" -> ".join(elementos) + " -> None")
        #Prueba
mi_lista = ListaEnlazada()

print("Estado inicial de la lista:")
mi_lista.mostrar()

print("\nAgregando elementos...")
mi_lista.agregar("Maria")
mi_lista.agregar("Pepe")
mi_lista.agregar("Marco")

print("Lista enlazada resultante:")
mi_lista.mostrar()