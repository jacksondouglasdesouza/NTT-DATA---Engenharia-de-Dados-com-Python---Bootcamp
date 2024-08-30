# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 07 - 29/08/2024
# Tipos de operadores com Python

# Operadores Aritméticos

# Adição (+) - Soma dois valores
# Subtração (-) - Subtrai um valor de outro
# Multiplicação (*) - Multiplica dois valores
# Divisão (/) - Divide um valor por outro
# Divisão inteira (//) - Divide um valor por outro e retorna a parte inteira
# Módulo (%) - Retorna o resto da divisão
# Exponenciação (**) - Eleva um valor a potência de outro

#Exemplos:

print(1 + 1)
print(2 - 1)
print(2 * 2)
print(4 / 2)
print(5 // 2)
print(5 % 2)
print(2 ** 2)

# Precedência aritmética - Python segue a mesma regra matemática

# 1. Parênteses
# 2. Exponenciação
# 3. Multiplicação e Divisão <<< Na ordem em que aparecem
# 4. Adição e Subtração <<< Na ordem em que aparecem

#Exemplos:

print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 * 4)
print(2 ** (3 * 4))
print(2 ** 3 ** 4)

print(10 - 5 * 2)
print((10 - 5) * 2)

print(10 ** 2 * 2)
print(10 ** (2 * 2))

print(10 / 2 * 4)

produto_01 = 20
produto_02 = 10

print(f'O valor total da compra é de R$ {produto_01 + produto_02}')
print(f'O valor total da compra é de R$ {produto_01 - produto_02}')
print(f'O valor total da compra é de R$ {produto_01 * produto_02}')
print(f'O valor total da compra é de R$ {produto_01 / produto_02}')
print(f'O valor total da compra é de R$ {produto_01 // produto_02}')
print(f'O valor total da compra é de R$ {produto_01 % produto_02}')
print(f'O valor total da compra é de R$ {produto_01 ** produto_02}')

print("\n")

