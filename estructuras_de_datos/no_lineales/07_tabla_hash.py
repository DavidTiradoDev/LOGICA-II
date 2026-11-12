# ============================================
# TABLA HASH / MAPA
# Pares clave -> valor con busqueda muy rapida
# ============================================
# En Python esto ya existe: es el diccionario (dict).
# Primero lo uso normal, y despues hago una tabla hash
# sencilla a mano para entender como funciona por dentro.

print("===== TABLA HASH (diccionario de Python) =====")

# Clave = nombre del estudiante, Valor = nota
notas = {}
notas["Ana"] = 4.5
notas["Luis"] = 3.2
notas["Maria"] = 5.0
print("Notas:", notas)

# Buscar es muy rapido: no hay que recorrer, se va directo a la clave
print("Nota de Maria:", notas["Maria"])

# Cambiar un valor
notas["Luis"] = 3.8
print("Le subi la nota a Luis:", notas)

# Preguntar si una clave existe
print("Esta Pedro?", "Pedro" in notas)

# Eliminar
del notas["Ana"]
print("Elimine a Ana:", notas)

# Recorrer
print("Recorriendo:")
for nombre, nota in notas.items():
    print("  ", nombre, "->", nota)


# ---------- Tabla hash hecha a mano ----------
print()
print("===== TABLA HASH HECHA A MANO =====")
# Idea: tengo un arreglo de "cubetas". Con una funcion hash
# convierto la clave en un numero, y ese numero me dice
# en que cubeta guardo el par (clave, valor).


class TablaHash:
    def __init__(self, tamano=5):
        self.tamano = tamano
        # cada cubeta es una lista, por si dos claves caen en la misma (colision)
        self.cubetas = []
        for i in range(tamano):
            self.cubetas.append([])

    # Funcion hash muy simple: sumo el codigo de cada letra y saco el residuo
    def funcion_hash(self, clave):
        suma = 0
        for letra in clave:
            suma += ord(letra)
        return suma % self.tamano

    def guardar(self, clave, valor):
        indice = self.funcion_hash(clave)
        cubeta = self.cubetas[indice]
        # si la clave ya existe, actualizo el valor
        for par in cubeta:
            if par[0] == clave:
                par[1] = valor
                return
        cubeta.append([clave, valor])

    def obtener(self, clave):
        indice = self.funcion_hash(clave)
        for par in self.cubetas[indice]:
            if par[0] == clave:
                return par[1]
        return None

    def mostrar(self):
        for i in range(self.tamano):
            print("   cubeta", i, ":", self.cubetas[i])


tabla = TablaHash()
tabla.guardar("Ana", 4.5)
tabla.guardar("Luis", 3.2)
tabla.guardar("Maria", 5.0)
tabla.guardar("Pedro", 2.9)

print("La clave 'Ana' va a la cubeta:", tabla.funcion_hash("Ana"))
print("La clave 'Luis' va a la cubeta:", tabla.funcion_hash("Luis"))
print("Asi quedo la tabla por dentro:")
tabla.mostrar()
print("Nota de Pedro:", tabla.obtener("Pedro"))
print("Nota de Carlos:", tabla.obtener("Carlos"))
