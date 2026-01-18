#Alfredo Noriega Aranda

# Creamos dos sets de ejemplo
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

# union() Une los elementos de dos sets
print("\n1. union()")
print(A.union(B))          # {1, 2, 3, 4, 5, 6}

# intersection() Elementos en común
print("\n2. intersection()")
print(A.intersection(B))   # {3, 4}

# difference() Elementos que están en A pero NO en B
print("\n3. difference()")
print(A.difference(B))     # {1, 2}

# symmetric_difference() Elementos NO compartidos entre A y B
print("\n4. symmetric_difference()")
print(A.symmetric_difference(B))  # {1, 2, 5, 6}

# add() Agregar elemento al set
print("\n5. add()")
A.add(10)
print(A)   # {1, 2, 3, 4, 10}

# remove() Eliminar un elemento (da error si no existe)
print("\n6. remove()")
A.remove(2)
print(A)   # {1, 3, 4, 10}
