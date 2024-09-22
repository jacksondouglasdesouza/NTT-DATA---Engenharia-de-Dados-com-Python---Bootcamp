# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 25 - 22/09/2024

# Conhecendo Tuplas em Python

# TUPLAS

"""
    Tuplas são estruturas de dados semelhantes às listas, mas com a diferença de serem imutáveis.
    Ou seja, uma vez que uma tupla é criada, não é possível adicionar, remover ou alterar elementos.
    
"""

# Criando uma tupla

tupla_frutas = ('banana', 'maçã', 'uva', 'laranja', 'abacaxi',)

letras_tupla = tuple("Curso de Python")

numeros_tupla = tuple([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

paises_tupla = tuple(['Brasil', 'Argentina', 'Chile', 'Uruguai', 'Paraguai', 'Peru', 'Colômbia', 'Venezuela',])

print(tupla_frutas)
print(letras_tupla)
print(numeros_tupla)
print(paises_tupla)

# Acessando elementos de uma tupla

print(tupla_frutas[0])
print(tupla_frutas[1])
print(tupla_frutas[2])
print(tupla_frutas[3])
print(tupla_frutas[4])

print(letras_tupla[0])
print(letras_tupla[1])
print(letras_tupla[2])
print(letras_tupla[3])
print(letras_tupla[4])

print(numeros_tupla[0])
print(numeros_tupla[1])
print(numeros_tupla[2])
print(numeros_tupla[3])
print(numeros_tupla[4])

print(paises_tupla[0])
print(paises_tupla[1])
print(paises_tupla[2])
print(paises_tupla[3])
print(paises_tupla[4])

# Acessando elementos de uma tupla com índices negativos


print(tupla_frutas[-1])
print(tupla_frutas[-2])
print(tupla_frutas[-3])
print(tupla_frutas[-4])

print(letras_tupla[-1])
print(letras_tupla[-2])
print(letras_tupla[-3])
print(letras_tupla[-4])

print(numeros_tupla[-1])
print(numeros_tupla[-2])
print(numeros_tupla[-3])
print(numeros_tupla[-4])

print(paises_tupla[-1])
print(paises_tupla[-2])
print(paises_tupla[-3])
print(paises_tupla[-4])


#Tuplas Aninhadas

tupla_aninhada = (
    (1, 2, 3, "a"),
    (4, 5,"b", 6),
    ("c",7, 8, 9),
)

print("\n")

print("ELEMENTOS DA TUPLA ANINHADA")

print(tupla_aninhada)

print(tupla_aninhada[0]) # (1, 2, 3, "a")
print(tupla_aninhada[1]) # (4, 5,"b", 6)
print(tupla_aninhada[2]) # ("c",7, 8, 9)
print(tupla_aninhada[0][0]) # 1
print(tupla_aninhada[0][1]) # 2
print(tupla_aninhada[0][2]) # 3
print(tupla_aninhada[1][0]) # 4
print(tupla_aninhada[1][1]) # 5
print(tupla_aninhada[1][2]) # "b"
print(tupla_aninhada[1][3]) # 6
print(tupla_aninhada[2][0]) # "c"
print(tupla_aninhada[2][1]) # 7
print(tupla_aninhada[2][2]) # 8
print(tupla_aninhada[2][3]) # 9

# fatiamento de tuplas
print("\n")
print("FATIAMENTO DE TUPLAS")
print(tupla_frutas)
print(tupla_frutas[0:3])
print(tupla_frutas[:3])
print(tupla_frutas[3:])
print(tupla_frutas[:])
print(tupla_frutas[::])
print(tupla_frutas[1:4])
print(tupla_frutas[1:4:2])
print(tupla_frutas[::-1])
print(tupla_frutas[::-2])
print("\n")

# Iterando sobre uma tupla

for fruta in tupla_frutas:
    print(fruta)
#--

for letra in letras_tupla:
    print(letra)
#--

for numero in numeros_tupla:
    print(numero)
#--

for indice, pais in enumerate(paises_tupla):
    print(f"O país {pais} está na posição {indice}")
#--


# Count e Index

print(tupla_frutas.count('banana'))
print(tupla_frutas.index('banana'))

print(letras_tupla.count('o'))
print(letras_tupla.index('o'))

print(numeros_tupla.count(100))
print(numeros_tupla.index(100))

print(paises_tupla.count('Brasil'))
print(paises_tupla.index('Brasil'))

# Len, Min e Max

print(len(tupla_frutas))
print(min(tupla_frutas))
print(max(tupla_frutas))

print(len(letras_tupla))
print(min(letras_tupla))
print(max(letras_tupla))