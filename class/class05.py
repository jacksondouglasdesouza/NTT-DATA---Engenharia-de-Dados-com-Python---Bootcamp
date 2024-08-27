# Input and Output

nome = input("Digite seu nome: ")
print(f'Seu nome é {nome}')

# Função  Built-in input() sempre retorna uma string
# Para converter para outro tipo, é necessário fazer a conversão explicita

idade = int(input("Digite sua idade: "))
print(f'Sua idade é {idade}')

#Função de output Built-in print()
# print() pode receber vários argumentos
# print() pode receber argumentos nomeados
# print() pode receber argumentos de formatação
# print() pode receber argumentos de formatação nomeados

print('a', 'b', 'c', sep='-', end='\n')
print('d', 'e', 'f')

