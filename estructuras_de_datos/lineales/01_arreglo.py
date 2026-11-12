# ============================================
# ARREGLO (ARRAY)
# Tamaño fijo, acceso por posición
# ============================================
# En Python no hay arreglos de tamaño fijo "puros" como en C o Java,
# asi que lo simulo con una lista que creo con un tamaño definido
# y no la dejo crecer.

print("===== ARREGLO =====")

# Creo un arreglo de 5 posiciones, todas vacias (None)
TAMANO = 5
arreglo = [None] * TAMANO
print("Arreglo vacio:", arreglo)

# Guardo valores en cada posicion (los indices empiezan en 0)
arreglo[0] = 10
arreglo[1] = 20
arreglo[2] = 30
arreglo[3] = 40
arreglo[4] = 50
print("Arreglo con datos:", arreglo)

# Acceso por posicion: es directo, no hay que recorrer nada
print("El elemento en la posicion 2 es:", arreglo[2])

# Modifico un valor
arreglo[2] = 99
print("Cambie la posicion 2 por 99:", arreglo)

# Recorro el arreglo con un for
print("Recorriendo el arreglo:")
for i in range(TAMANO):
    print("  posicion", i, "->", arreglo[i])

# Buscar un valor (busqueda lineal)
buscado = 40
encontrado = False
for i in range(TAMANO):
    if arreglo[i] == buscado:
        print("Encontre el", buscado, "en la posicion", i)
        encontrado = True
if not encontrado:
    print("No encontre el", buscado)

# Que pasa si me salgo del tamaño?
print("Intentando acceder a la posicion 10...")
try:
    print(arreglo[10])
except IndexError:
    print("  Error: esa posicion no existe, el arreglo solo tiene", TAMANO, "posiciones")
