# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 23 - 21/09/2024

# Listas: Criação e acesso aos dados
'''
    Listas em Python são coleções de itens em uma ordem específica. que podem armazenar vários tipos de dados.
    de maneira sequencial. Listas são mutáveis, ou seja, podem ser alteradas após a sua criação.
    Podemos criar listas utilizando o construtor list() ou utilizando colchetes [].
    A função range() é muito utilizada para criar listas de números inteiros.
'''

# EXEMPLOS

frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
frutas.append('morango')
print(frutas)
print(len(frutas))

#--


letras_palavra= list('Curso de Python') # Cria uma lista de caracteres a partir da frase
print(letras_palavra)
print(len(letras_palavra))

#--

numeros_predefinidos = list(range(11)) # Cria uma lista de números de 0 a 10
print(numeros_predefinidos)

#--

# LISTAS ANINHADAS

# Listas aninhadas são listas que contém outras listas como elementos.
# Podemos acessar os elementos internos utilizando índices múltiplos.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][1]) # Acessa o elemento 5
print(matriz[2][0]) # Acessa o elemento 7
print(matriz[0]) # Acessa o elemento [1, 2, 3]
print(matriz[1]) # Acessa o elemento [4, 5, 6]
print(matriz[2]) # Acessa o elemento [7, 8, 9]

#Fatias de listas

lista_palavras = ["P", "Y", "T", "H", "O", "N"]

lista_palavras[2:] # Retorna ['T', 'H', 'O', 'N']
lista_palavras[:2] # Retorna ['P', 'Y']
lista_palavras[1:3] # Retorna ['Y', 'T'] Posição Final - 1 por padrão
lista_palavras[0:3:2] # Retorna ['P', 'T'] Posição Final - 1 por padrão | Pula de 2 em 2 casas
lista_palavras[::] # Retorna ['P', 'Y', 'T', 'H', 'O', 'N'] Retorna a lista inteira como cópia
lista_palavras[::-1] # Retorna ['N', 'O', 'H', 'T', 'Y', 'P'] Retorna a lista completa invertida

print(lista_palavras[2:])
print(lista_palavras[:2])
print(lista_palavras[1:3])
print(lista_palavras[0:3:2])
print(lista_palavras[::])
print(lista_palavras[::-1])

for lista_py in lista_palavras:
    print(lista_py)
#--

print(" \n ")
# ENUMEATE

for indice, lista_palavras in enumerate(lista_palavras):
    print(F'Posição: {indice} -> Valor: {lista_palavras}')
#--

# LISTAS COMPREHENSIONS

# Listas comprehensions são uma forma concisa de criar listas em Python.
# São utilizadas para criar listas de forma mais rápida e eficiente.
# Podemos adicionar condicionais e loops for em listas comprehensions.

# EXEMPLOS

# VERSÃO 01
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 21, 65, 99, 113]
numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    #--
#--

print(numeros_pares)

# VERSÃO 02

print(' \n')
numeros_pares_comprehe = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares_comprehe)


# VERSÃO 03 - Modificando os valores da lista
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
#--

print(numeros)
print(quadrado)

#--

print(' \n')

quadrado_comprehe = [numero ** 2 for numero in numeros]

print(quadrado_comprehe)
print(numeros)
