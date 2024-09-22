# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 24 - 21/09/2024

# Listas: Métodos da classe list


# copy()

lista_01 = [100, "Douglas", True, 100.5, [50, 66, 778], "Maçã"]
print(lista_01)

#--

print(" \n ")

lista_01.append("Banana")
print(lista_01)

#--

print(" \n ")

lista_01.append(["Carro, Moto, Bicicleta"])
print(lista_01)

#-- 

li_01= lista_01.copy()
0
print(" \n ")

print(id(lista_01))
print(id(li_01))

print(" \n ")

print(f'Cópia da lista: {li_01}')

# Clear()

li_01.clear()

print(" \n ")

print(f'Lista após o método clear: {li_01} <<< Esta vazia')

#count()

cores_lista = ["vermelho", "verde", "azul", "vermelho", "amarelo", "vermelho", "azul", "vermelho", "verde", "vermelho"]

print(" \n ")
print(cores_lista)
print(" \n ")
print(cores_lista.count("vermelho"))
print(cores_lista.count("azul"))
print(cores_lista.count("verde"))

#extend()

lingua = ["Português", "Inglês", "Espanhol"]
print(" \n ")
print(lingua)

lingua.extend(["Francês", "Italiano", "Alemão"])

print(" \n ")
print(lingua)

#index()
print(" \n ")

print(lingua.index("Inglês"))
print(lingua.index("Francês"))
print(lingua.index("Alemão"))

#pop()

lita_pop = ["Carro", "Moto", "Bicicleta", "Avião", "Navio", "Trem", "Ônibus", "Caminhão", "Barco", "Helicóptero"]
print(" \n ")
print(lita_pop)

print(" \n ")

print(lita_pop.pop())
print(lita_pop.pop())
print(lita_pop)
print(" \n ")
print(lita_pop.pop(2)) # Bicicleta
print(lita_pop)
print(" \n ")
print(lita_pop.pop(0)) # Carro
print(lita_pop)

#-- 

#remove()

lista_remove = ["Carro", "Moto", "Bicicleta", "Avião", "Navio", "Trem", "Ônibus", "Caminhão", "Barco", "Helicóptero"]

lista_remove.remove("Carro")
print(" \n ")
print(lista_remove)

lista_remove.remove("Bicicleta")
print(" \n ")
print(lista_remove)

# Reverse()

lista_reverse = ["Carro", "Moto", "Bicicleta", "Avião", "Navio", "Trem", "Ônibus", "Caminhão", "Barco", "Helicóptero"]

print(" \n ")
print(lista_reverse)
print(" \n ")
lista_reverse.reverse()
print(lista_reverse)

#--

print(" \n ")

# Sort()

#lista_sort = [100, 50, 200, 300, 150, 250, 350, 400, 450, 500]
lista_sort = ["C", "C++", "C#", "Java", "Python", "Ruby", "JavaScript", "PHP", "Swift", "Kotlin"]
lista_sort.sort()
print(lista_sort)

#--

print(" \n ")

lista_sort.sort(reverse=True)
print(lista_sort)

#--

print(" \n ")

lista_sort.sort(reverse=False)
print(lista_sort)

#--

print(" \n ")

lista_sort.sort(key=lambda x: len(x))
print(lista_sort)

#--

print(" \n ")

lista_sort.sort(key=lambda x: len(x), reverse=True)
print(lista_sort)

#--

#LEN()

print(" \n ")

print(len(lista_sort))

# sorted()

lista_sorted_completa = ["C", "C++", "C#", "Java", "Python", "Ruby", "JavaScript", "PHP", "Swift", "Kotlin", "Camel", "TypeScript", "Rust", "Go", "Scala", "Perl", "Lua", "R", "Objective-C", "Haskell", "Elixir", "Clojure", "F#", "Dart", "Groovy", "Julia", "Kotlin", "Racket", "Scheme", "Smalltalk", "Erlang", "Prolog", "Lisp", "Fortran", "COBOL", "Pascal", "Ada", "Algol", "Simula", "BCPL", "PL/I", "APL", "SNOBOL"]

print(" \n ")

print(lista_sorted_completa)

lista_sorted_completa.sort()

print(" \n ")

print(lista_sorted_completa)