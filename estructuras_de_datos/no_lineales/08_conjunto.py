# ============================================
# CONJUNTO (SET)
# Elementos sin repetir
# ============================================
# En Python existe el tipo set.
# Si meto un elemento repetido, simplemente lo ignora.
# Ojo: un set NO tiene orden, asi que no puedo hacer conjunto[0].

print("===== CONJUNTO =====")

# Creo un conjunto a partir de una lista con repetidos
lista_con_repetidos = [1, 2, 2, 3, 3, 3, 4]
conjunto = set(lista_con_repetidos)
print("Lista original:", lista_con_repetidos)
print("Como conjunto:", conjunto)

# Agregar elementos
conjunto.add(5)
conjunto.add(2)  # este ya estaba, no pasa nada
print("Agregue 5 y 2 (el 2 ya estaba):", conjunto)

# Preguntar si un elemento esta (es muy rapido, como en la tabla hash)
print("Esta el 3?", 3 in conjunto)
print("Esta el 10?", 10 in conjunto)

# Eliminar
conjunto.remove(1)
print("Elimine el 1:", conjunto)
print("Cantidad de elementos:", len(conjunto))

# ---------- Operaciones de conjuntos (como en matematicas) ----------
print()
print("Operaciones entre conjuntos")
print("Ejemplo: estudiantes en dos materias")

logica = {"Ana", "Luis", "Maria", "Pedro"}
calculo = {"Maria", "Pedro", "Sofia", "Carlos"}
print("  Logica:", logica)
print("  Calculo:", calculo)

# Union: los que estan en alguna de las dos
print("  Union (ven alguna materia):", logica | calculo)

# Interseccion: los que estan en las dos
print("  Interseccion (ven las dos):", logica & calculo)

# Diferencia: los que estan en logica pero no en calculo
print("  Diferencia (solo logica):", logica - calculo)

# Diferencia simetrica: los que ven solo una de las dos
print("  Diferencia simetrica (solo una):", logica ^ calculo)

# ---------- Uso practico ----------
print()
print("Uso practico: contar palabras distintas")
frase = "el perro y el gato y el raton"
palabras = frase.split()
distintas = set(palabras)
print("  Frase:", frase)
print("  Total de palabras:", len(palabras))
print("  Palabras distintas:", len(distintas), "->", distintas)
