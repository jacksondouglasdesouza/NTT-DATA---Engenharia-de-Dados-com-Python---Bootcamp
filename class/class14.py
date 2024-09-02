# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 14 - 30/08/2024

# Estruturas Condicionais e de Repetição em Python

# Estruturas Condicionais

# IF | IF-ELSE | ELSE E IF TERNÁRIO

saldo = 2000
saque = float(input('Digite o valor do saque: '))

if saldo >= saque:
    saldo = saldo - saque
    print('Saque realizado com sucesso!')
else:
    print('Saldo insuficiente!')
#--

print('Saldo atual: R$ {:.2f}'.format(saldo))

#--


# Exemplo com elif

saldo_dois = 5000

opcao = int(input("Escolha uma das opções: \n[ 1 ] - Saque  \n[ 2 ] - Depósito  \n[ 3 ] - Saldo "))

if opcao == 1:
    print('Opção escolhida: Saque')
    saque = float(input('Digite o valor do saque: '))
    if saldo_dois >= saque:
        saldo = saldo - saque
        print(f'Saque de R${saque} realizado com sucesso!')
    else:
        print('Saldo insuficiente para realizar esta operação!')
    #--
elif opcao == 2:
    value_deposito = float(input('Digite o valor do depósito: '))
    saldo_dois = saldo_dois + value_deposito
    print(f'Depósito de R${value_deposito} realizado com sucesso!')
elif opcao == 3:
    print(f'Saldo atual: R${saldo_dois}')
else:
    print('Opção inválida!')
#--


#-- outro exemplo

MAIOR_IDADE = 18

idade = int(input('Digite a sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')
#--

# if ternário

idade = int(input('Digite a sua idade: '))

print('Você é maior de idade!' if idade >= MAIOR_IDADE else 'Você é menor de idade!')

# Outro exemplo

saldo = 2000
saque = float(input('Digite o valor do saque: '))
print('Saque realizado com sucesso!' if saldo >= saque else 'Saldo insuficiente!')
print('Saldo atual: R$ {:.2f}'.format(saldo))


