"""
ESTRUCTURA DE DATOS: Array Unidimensional (Vector)
CONCEPTO CLAVE: Colección lineal de elementos indexados desde 0 hasta (tamaño - 1).
OPERACIONES FUNDAMENTALES:
    - Crear: Inicializa el arreglo (con tamaño o elementos iniciales).
    - Agregar: Inserta un dato al final o en un índice válido.
    - Eliminar: Retira un dato por su índice o valor.
    - Buscar: Localiza la posición de un elemento (búsqueda lineal O(n)).
    - Ordenar: Organiza los elementos según un criterio.
"""


class Arreglo:
    """Implementación del TDA Arreglo Unidimensional basado en listas de Python."""

    def __init__(self, elementos_iniciales=None):
        """1. CREAR: Inicializa la estructura de datos."""
        if elementos_iniciales is None:
            self.elementos = []
        else:
            self.elementos = list(elementos_iniciales)

    # -------------------------------------------------------------
    # 2. AGREGAR / INSERTAR
    # -------------------------------------------------------------
    def agregar(self, valor):
        """Agrega un elemento al final del arreglo. O(1) amortizado."""
        self.elementos.append(valor)

    def insertar(self, indice, valor):
        """Inserta en una posición específica desplazando los demás. O(n)."""
        if 0 <= indice <= len(self.elementos):
            self.elementos.insert(indice, valor)
        else:
            raise IndexError("Índice fuera del rango permitido.")

    # -------------------------------------------------------------
    # 3. ELIMINAR
    # -------------------------------------------------------------
    def eliminar_por_indice(self, indice):
        """Elimina y retorna el dato en el índice indicado. O(n)."""
        if self.is_empty():
            raise IndexError("El arreglo está vacío.")
        if not (0 <= indice < len(self.elementos)):
            raise IndexError("Índice fuera de límites.")
        return self.elementos.pop(indice)

    # -------------------------------------------------------------
    # 4. BUSCAR Y ACCEDER
    # -------------------------------------------------------------
    def obtener(self, indice):
        """Acceso directo por índice numérico (base + desplazamiento). O(1)."""
        if not (0 <= indice < len(self.elementos)):
            raise IndexError("Índice fuera de límites.")
        return self.elementos[indice]

    def buscar(self, valor):
        """Busca secuencialmente un valor y devuelve su índice. O(n)."""
        for i in range(len(self.elementos)):
            if self.elementos[i] == valor:
                return i  # Retorna el índice donde lo encontró
        return -1  # Retorna -1 si no existe en el arreglo

    # -------------------------------------------------------------
    # 5. ORDENAR
    # -------------------------------------------------------------
    def ordenar(self, descendente=False):
        """Ordena los elementos de menor a mayor (o viceversa). O(n log n)."""
        self.elementos.sort(reverse=descendente)

    # -------------------------------------------------------------
    # MÉTODOS AUXILIARES
    # -------------------------------------------------------------
    def tamano(self):
        """Retorna la cantidad total de elementos."""
        return len(self.elementos)

    def is_empty(self):
        """Verifica si la estructura no contiene datos."""
        return len(self.elementos) == 0

    def __str__(self):
        """Representación visual del vector."""
        return str(self.elementos)


# =====================================================================
# EJEMPLO EN LA VIDA REAL: CONTROL DE CALIFICACIONES DE UN GRUPO
# =====================================================================

def demostracion_caso_real():
    print("=== GESTIÓN DE CALIFICACIONES ESCOLARES (TDA ARREGLO) ===\n")

    # 1. Crear el arreglo inicial
    calificaciones = Arreglo([8.5, 9.0, 7.2, 10.0, 6.5])
    print(f"Vector inicial creado: {calificaciones}")
    print(f"Total de alumnos (tamaño): {calificaciones.tamano()}")

    # 2. Acceso instantáneo O(1)
    # Según el apunte: primer índice 0, último índice tamaño - 1
    primer_alumno = calificaciones.obtener(0)
    ultimo_alumno = calificaciones.obtener(calificaciones.tamano() - 1)
    print(f"\n[Acceso O(1)] Primer índice (0): {primer_alumno}")
    print(f"[Acceso O(1)] Último índice ({calificaciones.tamano() - 1}): {ultimo_alumno}")

    # 3. Agregar nuevos datos
    calificaciones.agregar(9.5)
    print(f"\n[Agregar] Alumno nuevo añadido al final: {calificaciones}")

    # 4. Buscar un elemento O(n)
    nota_a_buscar = 10.0
    posicion = calificaciones.buscar(nota_a_buscar)
    if posicion != -1:
        print(f"[Buscar] La calificación {nota_a_buscar} se encuentra en el índice {posicion}.")

    # 5. Ordenar el arreglo
    print("\n[Ordenar] Ordenando calificaciones de mayor a menor...")
    calificaciones.ordenar(descendente=True)
    print(f"Vector ordenado: {calificaciones}")

    # 6. Eliminar un elemento
    expulsado = calificaciones.eliminar_por_indice(0)  # Quitamos la nota más alta
    print(f"\n[Eliminar] Se dio de baja la nota {expulsado}.")
    print(f"Estado final del arreglo: {calificaciones}")


if __name__ == "__main__":
    demostracion_caso_real()