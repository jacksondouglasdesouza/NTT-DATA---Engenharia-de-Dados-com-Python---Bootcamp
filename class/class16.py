# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 16 - 01/09/2024
'''

    Conhecendo métodos úteis da classe string
Manipulando Strings com Python

'''

curso = 'Python'

print(curso.upper())
print(curso.lower())
print(curso.capitalize())
print(curso.title())
print(curso.swapcase())

#--

print("")

#--

curso_dois = "     Python      "
print(curso.strip())
print(curso.rstrip())
print(curso.lstrip())

#--

curso_tres = "Python"

print(" ")
(print(curso_tres.center(10, '*')))

print(" ")

print('...'.join(curso_tres))

nome = "Jackson Douglas"

print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.title())
print(nome.swapcase())

texto = "   -  é uma linguagem de programação | -   " + "."

print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

#--

print(" ")

#-- 

curso_quatro = " - Python - "

print(curso_quatro.center(20, '*')) 

curso_cinco = "Python"

print('...'.join(curso_cinco))


