# ============================================
# ARBOL
# Jerarquia de padres e hijos (carpetas, menus)
# ============================================
# Cada nodo tiene un valor y una lista de hijos.
# El nodo de arriba del todo se llama "raiz".
# Los nodos que no tienen hijos se llaman "hojas".


class NodoArbol:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


# Funcion para imprimir el arbol con sangria segun el nivel
# Uso recursion: la funcion se llama a si misma para cada hijo
def mostrar_arbol(nodo, nivel=0):
    print("    " * nivel + "|-- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)


# Funcion para buscar un nodo por nombre
def buscar(nodo, nombre):
    if nodo.nombre == nombre:
        return True
    for hijo in nodo.hijos:
        if buscar(hijo, nombre):
            return True
    return False


# Funcion para contar cuantos nodos hay
def contar_nodos(nodo):
    total = 1  # me cuento a mi mismo
    for hijo in nodo.hijos:
        total += contar_nodos(hijo)
    return total


# ---------- Probando el arbol ----------
print("===== ARBOL =====")
print("Ejemplo: carpetas de un computador")
print()

# Creo los nodos
raiz = NodoArbol("C:")
documentos = NodoArbol("Documentos")
musica = NodoArbol("Musica")
universidad = NodoArbol("Universidad")
logica = NodoArbol("logica_II.py")
tarea = NodoArbol("tarea1.docx")
cancion = NodoArbol("cancion.mp3")

# Armo la jerarquia (quien es hijo de quien)
raiz.agregar_hijo(documentos)
raiz.agregar_hijo(musica)
documentos.agregar_hijo(universidad)
universidad.agregar_hijo(logica)
universidad.agregar_hijo(tarea)
musica.agregar_hijo(cancion)

mostrar_arbol(raiz)

print()
print("Existe 'tarea1.docx'?", buscar(raiz, "tarea1.docx"))
print("Existe 'foto.png'?", buscar(raiz, "foto.png"))
print("Total de nodos en el arbol:", contar_nodos(raiz))
print("La raiz es:", raiz.nombre)
print("Los hijos de la raiz son:", [h.nombre for h in raiz.hijos])
