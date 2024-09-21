# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 22 - 21/09/2024

#positional only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
#-

criar_carro('Fusca', 1970, 'ABC-1234', 'Volkswagen', '1.6', 'Gasolina')
criar_carro('Fusca', 1970, 'ABC-1234', marca='Volkswagen', motor='1.8', combustivel='Diesel')

# Keyword only

def criar_carro_02(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
#-

print(" ")
criar_carro_02(modelo='Fusca', ano=1970, placa='ABC-1234', marca='Volkswagen', motor='1.6', combustivel='Gasolina')

print(" ")

# kyword and positional only - Ibridos

def criar_carro_03(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
#-

criar_carro_03('Fusca', 1970, 'ABC-1234', marca='Volkswagen', motor='1.6', combustivel='Gasolina')

def criar_carro_04(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
#-

criar_carro_04('Fusca', 1970, 'ABC-1234', 'Volkswagen', motor='1.6', combustivel='Gasolina')
criar_carro_04('Fusca', 1970, 'ABC-1234', marca='Volkswagen', motor='1.6', combustivel='Gasolina')

# Objetos de primeira classe

def somar(a, b):
    return a + b
#-

def subtrair(a, b):
    return a - b
#-

def exibir_resultado(funcao, a, b):
    resultado = funcao(a, b)
    print(resultado)
#-

def multiplicar(a, b):
    return a * b
#-

def dividir(a, b):
    return a / b
#-

exibir_resultado(somar, 10, 20)
exibir_resultado(lambda a, b: a * b, 10, 20)
exibir_resultado(subtrair, 10, 20)
exibir_resultado(multiplicar, 10, 20)
exibir_resultado(dividir, 10, 20)


# Escopo global e local

def funcao():
    variavel_local = 'Local'
    print(variavel_local)
#-

funcao()

variavel_global = 'Global'
salario = 1000

def funcao_02():
    global salario
    print(variavel_global)
    print(salario)
#-

funcao_02()

def funcao_03(bonus):
    global salario
    salario += bonus
    print(salario)
#-

funcao_03(500)
