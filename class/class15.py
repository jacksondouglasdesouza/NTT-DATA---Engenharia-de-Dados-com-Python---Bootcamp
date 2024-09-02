# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 15 - 30/08/2024

# Estruturas Condicionais e de Repetição em Python

# Estruturas de Repetição

# FOR | WHILE E FUNÇÃO BUILT-IN RANGE()

texto = input('Digite um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
    #--
#--

print(" ")


print(list(range(10)))

# range(inicio, fim, passo)

for numero01 in range(0, 11, 2):
    print(numero01, end=' ')
#--

print(" ")

for numero in range(0, 101, 5):
    print(numero, end=' ')
#--

# Tabuada do 5

print(" ")

for numero03 in range(0, 11):
    print(f'5 x {numero03} = {5 * numero03}')
#--


# WHILE

value = -1

while value != 0:
    value = int(input('Qual operação deseja executar? \n[1] Sacar \n[2] Depositar \n[3] Saldo \n[0] Sair\n'))
    
    if value == 1:
        print('Sacar')
    elif value == 2:
        print('Depositar')
    elif value == 3:
        print('Saldo')
    elif value == 0:
        print('Sair')
    else:
        print('Opção inválida!')
    #--
#--

# ---------------------------- #

value_dois = -1

while value_dois != 0:
    value_dois = int(input('Digite um valor: '))
    
    if value_dois % 2 == 0:
        print('Valor par')
        break
    else:
        print('Valor ímpar')
    #--
#--

