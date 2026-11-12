# ============================================
# LISTA ENLAZADA
# Cada elemento (nodo) apunta al siguiente
# ============================================
# Un nodo tiene dos cosas:
#   - el dato que guarda
#   - una referencia al siguiente nodo
# El ultimo nodo apunta a None (no hay mas)


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # el primer nodo de la lista

    # Agregar al final de la lista
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            # si la lista esta vacia, el nuevo es el primero
            self.cabeza = nuevo
        else:
            # recorro hasta llegar al ultimo nodo
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Agregar al inicio de la lista
    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Buscar un dato
    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    # Eliminar un dato
    def eliminar(self, dato):
        if self.cabeza is None:
            return
        # si el que quiero borrar es el primero
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return
        # si no, busco el nodo anterior al que quiero borrar
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente  # me lo salto
                return
            actual = actual.siguiente

    # Mostrar la lista
    def mostrar(self):
        actual = self.cabeza
        texto = ""
        while actual is not None:
            texto += str(actual.dato) + " -> "
            actual = actual.siguiente
        texto += "None"
        print(texto)


# ---------- Probando la lista ----------
print("===== LISTA ENLAZADA =====")

lista = ListaEnlazada()
lista.agregar("A")
lista.agregar("B")
lista.agregar("C")
print("Agregue A, B y C:")
lista.mostrar()

lista.agregar_al_inicio("Z")
print("Agregue Z al inicio:")
lista.mostrar()

print("Esta B en la lista?", lista.buscar("B"))
print("Esta X en la lista?", lista.buscar("X"))

lista.eliminar("B")
print("Elimine B:")
lista.mostrar()
