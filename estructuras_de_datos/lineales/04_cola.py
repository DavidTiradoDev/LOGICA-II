# ============================================
# COLA (QUEUE)
# Primero en entrar, primero en salir (FIFO)
# ============================================
# Es como la fila del banco: el primero que llega
# es el primero que atienden.
# Los elementos entran por el final y salen por el inicio.


class Cola:
    def __init__(self):
        self.elementos = []

    # Entra alguien al final de la fila
    def encolar(self, dato):  # tambien se le dice "enqueue"
        self.elementos.append(dato)

    # Sale el primero de la fila
    def desencolar(self):  # tambien se le dice "dequeue"
        if self.esta_vacia():
            print("  La cola esta vacia, no hay nadie")
            return None
        return self.elementos.pop(0)  # saco el de la posicion 0

    # Ver quien es el primero sin sacarlo
    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)

    def mostrar(self):
        print("  Cola (frente a la izquierda):", self.elementos)


# ---------- Probando la cola ----------
print("===== COLA =====")

fila_banco = Cola()
fila_banco.encolar("Ana")
fila_banco.encolar("Luis")
fila_banco.encolar("Maria")
print("Llegaron Ana, Luis y Maria:")
fila_banco.mostrar()

print("El primero en la fila es:", fila_banco.ver_frente())

print("Atendiendo a:", fila_banco.desencolar())
fila_banco.mostrar()

fila_banco.encolar("Pedro")
print("Llego Pedro:")
fila_banco.mostrar()

print("Atendiendo a todos:")
while not fila_banco.esta_vacia():
    print("  Atendiendo a:", fila_banco.desencolar())

print("Intento atender con la cola vacia:")
fila_banco.desencolar()
