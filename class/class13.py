# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 07 - 30/08/2024

# Estruturas Condicionais e de Repetição em Python

# Indentação e Blocos de Código

saldo = 500

def sacar (valor):
    if saldo >= valor:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
    #--
#--

def depositar (value):
    saldo = 500
    saldo += value
    print('Depósito realizado com sucesso!')
#--

depositar(600)
print(saldo)
sacar(600)


