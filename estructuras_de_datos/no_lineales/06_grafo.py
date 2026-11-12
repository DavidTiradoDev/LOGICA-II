# ============================================
# GRAFO
# Nodos conectados entre si (redes sociales, mapas)
# ============================================
# A diferencia del arbol, aqui no hay "padre" ni "hijo":
# cualquier nodo se puede conectar con cualquier otro.
# Lo represento con un diccionario donde cada persona
# tiene una lista de sus amigos (lista de adyacencia).


class Grafo:
    def __init__(self):
        self.conexiones = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.conexiones:
            self.conexiones[nodo] = []

    # Conexion en los dos sentidos (si A es amigo de B, B es amigo de A)
    def conectar(self, a, b):
        self.agregar_nodo(a)
        self.agregar_nodo(b)
        self.conexiones[a].append(b)
        self.conexiones[b].append(a)

    def vecinos(self, nodo):
        return self.conexiones.get(nodo, [])

    def mostrar(self):
        for nodo in self.conexiones:
            print("  ", nodo, "esta conectado con:", self.conexiones[nodo])

    # Recorrido en anchura (BFS): primero los amigos, luego los amigos de los amigos...
    # Uso una COLA (lo que vimos en 04_cola.py)
    def recorrer(self, inicio):
        visitados = []
        cola = [inicio]
        while len(cola) > 0:
            actual = cola.pop(0)
            if actual not in visitados:
                visitados.append(actual)
                for vecino in self.conexiones[actual]:
                    if vecino not in visitados:
                        cola.append(vecino)
        return visitados

    # Saber si hay un camino entre dos nodos
    def hay_camino(self, a, b):
        return b in self.recorrer(a)


# ---------- Probando el grafo ----------
print("===== GRAFO =====")
print("Ejemplo: red social de amigos")
print()

red = Grafo()
red.conectar("Ana", "Luis")
red.conectar("Ana", "Maria")
red.conectar("Luis", "Pedro")
red.conectar("Maria", "Pedro")
red.conectar("Pedro", "Sofia")
red.agregar_nodo("Carlos")  # Carlos no tiene amigos :(

red.mostrar()

print()
print("Amigos de Pedro:", red.vecinos("Pedro"))
print("Recorriendo la red desde Ana:", red.recorrer("Ana"))
print("Ana puede llegar a Sofia?", red.hay_camino("Ana", "Sofia"))
print("Ana puede llegar a Carlos?", red.hay_camino("Ana", "Carlos"))
