# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 17 - 01/09/2024

'''
Interpolação de variáveis
Manipulando Strings com Python
'''

# Old Style %

name = 'João'
idade = 30
profissao = 'Engenheiro'
linguaqem = 'Python'

print('Olá, %s. Você tem %d anos e é %s. Você programa em %s.' % (name, idade, profissao, linguaqem))   

# Method format

print('Olá, {}. Você tem {} anos e é {}. Você programa em {}.'.format(name, idade, profissao, linguaqem))

# Method format with index

print('Olá, {0}. Você tem {1} anos e é {2}. Você programa em {3}.'.format(name, idade, profissao, linguaqem))

# Method format with named arguments

print('Olá, {name}. Você tem {idade} anos e é {profissao}. Você programa em {linguaqem}.'.format(name=name, idade=idade, profissao=profissao, linguaqem=linguaqem))
# Method format dictionary

locals = {'name': 'João', 'idade': 30, 'profissao': 'Engenheiro', 'linguaqem': 'Python'}

print('Olá, {name}. Você tem {idade} anos e é {profissao}. Você programa em {linguaqem}.'.format(**locals))


# f-strings

print(f'Olá, {name}. Você tem {idade} anos e é {profissao}. Você programa em {linguaqem}.')

#-- 

# Formatação da f' string

PI = 3.14159265359

print(f'O valor de PI é {PI:.2f}')
print(f'O valor de PI é {PI:.3f}')
print(f'O valor de PI é {PI:.4f}')
print(f'O valor de PI é {PI:.5f}')
print(f'O valor de PI é {PI:.6f}')

#--

print(f'O valor de PI é {PI:10.2f} e o dobro é {PI*2:10.2f}')
