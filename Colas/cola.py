from collections import deque

# 1. CREACIÓN: Inicializar la cola directamente
cola_banco = deque()

# 2. ENCOLAR (Enqueue): .append() mete elementos por el final O(1)
cola_banco.append("Cliente 1 (Pedro)")
cola_banco.append("Cliente 2 (Lucía)")
cola_banco.append("Cliente 3 (Mario)")

# 3. VER EL FRENTE (Peek): Consultar el índice 0 sin sacarlo O(1)
siguiente = cola_banco[0]
print(f"Siguiente en turno: {siguiente}")

# 4. TAMAÑO Y ESTADO: Funciones estándar len() y evaluación booleana
print(f"Personas formadas: {len(cola_banco)}")
if cola_banco:
    print("La cola tiene turnos pendientes.")

# 5. DESENCOLAR (Dequeue): .popleft() retira y devuelve el frente en O(1)
atendido = cola_banco.popleft()
print(f"Atendiendo en ventanilla a: {atendido}")

# Al imprimir directamente el objeto deque, muestra su contenido
print("Estado de la cola restante:", cola_banco)