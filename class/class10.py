# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 07 - 29/08/2024
# Tipos de operadores em Python

# Operadores lógicos

# Operador AND
# Operador OR
# Operador NOT

# Exemplos:

saldo = 1000
saque = 250
limite = 200
conta_especial = True

#true and true = true
#true and false = false
#false and true = false
#false and false = false

print(saldo >= saque and saque <= limite) # False (False and True = False)

#NOT 

# not true = false
# not false = true
print(not saldo >= saque) # False (not True = False)

contatos = []
print(not contatos) # True (not False = True)
aleatorio = ''
print(not aleatorio) # True (not False = True)

#--

print(f'Comparação: {saldo >= saque and saque <= limite or conta_especial and saldo >= saque}') # True

print(f'Comparação: {(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)}') # True


