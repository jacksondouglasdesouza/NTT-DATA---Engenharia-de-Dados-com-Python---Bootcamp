# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 26 - 22/09/2024

# Explorando Conjuntos em Python

# Conjuntos são coleções de elementos únicos e não ordenados
# Conjuntos são mutáveis, mas seus elementos devem ser imutáveis
# Conjuntos não aceitam elementos duplicados
# Conjuntos são representados por chaves {}

s1 = {1, 2, 3, 4, 5, 7, 1, 2, 3, 4, 5, 6, 7} # Conjunto com elementos duplicados // {1, 2, 3, 4, 5}
s2 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

print(s1)

for s in s1:
    print(s)
#--

s1.add(6) # Adiciona um elemento ao conjunto

print(s1)


s1.remove(3) # Remove um elemento do conjunto

print(s1)

s1.discard(5) # Remove um elemento do conjunto

print(s1)

s1.update("Casa da mãe Joana") # Adiciona vários elementos ao conjunto

print(s1)

s1.update([7, 8, 9, 10]) # Adiciona vários elementos ao conjunto

print(s1)

lista_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, "Carlos", "Casa", "Carlos"]) # Converte uma lista em conjunto

print(lista_set)

#add() - Adiciona um elemento ao conjunto
#remove() - Remove um elemento do conjunto
#discard() - Remove um elemento do conjunto
#update() - Adiciona vários elementos ao conjunto
#set() - Converte uma lista em conjunto
#clear() - Limpa o conjunto
#copy() - Copia o conjunto
#pop() - Remove um elemento aleatório do conjunto
#union() - União de conjuntos
#difference() - Diferença de conjuntos
#symmetric_difference() - Diferença simétrica
#intersection() - Interseção de conjuntos

# Simbolos

# | - União de conjuntos
# - - Diferença de conjuntos
# ^ - Diferença simétrica
# & - Interseção de conjuntos
# <= - Subconjunto
# >= - Superconjunto
# == - Igualdade de conjuntos
#-- >>>    != - Diferença de conjuntos
# < - Subconjunto próprio
# > - Superconjunto próprio
# in - Pertinência
# not in - Não pertinência

set01 = {1, 2, 3, 4, 5, 11}
set02 = {1, 2, 3, 4, 5, 6, 7, 8, 22}

#set03 = set01.union(set02) # União de conjuntos
set3 = set01 | set02 # União de conjuntos

print(set3)

set4 = set01 - set02 # Diferença de conjuntos
print(set4)

set5 = set02 - set01 # Diferença de conjuntos
print(sorted(set5))

set6 = set01 ^ set02 # Diferença simétrica
print(sorted(set6))

set7 = set01 & set02 # Interseção de conjuntos
print(sorted(set7))
