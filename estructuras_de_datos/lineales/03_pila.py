# ============================================
# PILA (STACK)
# Ultimo en entrar, primero en salir (LIFO)
# ============================================
# Es como una pila de platos: el ultimo plato que pongo
# encima es el primero que saco.
# Uso una lista de Python y solo trabajo por el final (el "tope").


class Pila:
    def __init__(self):
        self.elementos = []

    # Meter un elemento arriba
    def apilar(self, dato):  # tambien se le dice "push"
        self.elementos.append(dato)

    # Sacar el elemento de arriba
    def desapilar(self):  # tambien se le dice "pop"
        if self.esta_vacia():
            print("  La pila esta vacia, no hay nada que sacar")
            return None
        return self.elementos.pop()

    # Ver el de arriba sin sacarlo
    def ver_tope(self):  # tambien se le dice "peek"
        if self.esta_vacia():
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)

    def mostrar(self):
        print("  Pila (tope a la derecha):", self.elementos)


# ---------- Probando la pila ----------
print("===== PILA =====")

pila = Pila()
pila.apilar("plato 1")
pila.apilar("plato 2")
pila.apilar("plato 3")
print("Apile 3 platos:")
pila.mostrar()

print("El de arriba es:", pila.ver_tope())

print("Saco uno:", pila.desapilar())
pila.mostrar()

print("Saco otro:", pila.desapilar())
pila.mostrar()

print("Saco otro:", pila.desapilar())
pila.mostrar()

print("Intento sacar con la pila vacia:")
pila.desapilar()

# Ejemplo practico: invertir una palabra con una pila
print()
print("Ejemplo: invertir una palabra")
palabra = "python"
p = Pila()
for letra in palabra:
    p.apilar(letra)
invertida = ""
while not p.esta_vacia():
    invertida += p.desapilar()
print(" ", palabra, "->", invertida)
