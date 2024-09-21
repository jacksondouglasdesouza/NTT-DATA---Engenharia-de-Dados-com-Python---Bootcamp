# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 20 - 18/09/2024

#FUNÇÕES EM PYTHON

def exibir_mensagem():
    print('Olá, mundo!')
#-

def exibir_mensagem_nome(nome):
    print(f'Olá, {nome}!')
#-

def exibir_mensagem_nome_idade(nome, idade):
    print(f'Olá, {nome}! Você tem {idade} anos.')
#-

def nome__predefinido(nome='Edmundo'):
    print(f'Olá, {nome}!')
#-

exibir_mensagem() # Olá, mundo!
exibir_mensagem_nome('João') # Olá, João!
exibir_mensagem_nome_idade('Maria', 25) # Olá, Maria! Você tem 25 anos.
nome__predefinido() # O nome foi predefinido como Edmundo
nome__predefinido('José') # O nome foi alterado para José
#-


#FUNÇÕES COM RETORNO

def calcular_total(numeros):
    total = sum(numeros)
    return print(total)
#-

def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return print(media)
#-

def retorna_antececessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return print(antecessor), print(sucessor)
#-

calcular_total([1, 2, 3, 4, 5]) # 15
calcular_media([1, 2, 3, 4, 5]) # 3.0
retorna_antececessor_sucessor(5) # 4, 6
#-

# Argumentos nomeados

def exibir_nome_sobrenome(nome, sobrenome):
    print(f'Nome: {nome} Sobrenome: {sobrenome}')
#-

def values_carro(marca, modelo, ano, placa):
    print("O carro foi inserido com sucesso!")
    print(f'Marca: {marca} | Modelo: {modelo} | Ano: {ano} | Placa: {placa}')
#-

values_carro('Fiat', 'Uno', 2020, 'ABC-1234');
values_carro(marca='Fiat', modelo='Uno', ano=2020, placa='ABC-1234');
values_carro(ano=2020, placa='ABC-1234', marca='Fiat', modelo='Uno');
#-
values_carro(**{'marca': 'Fiat', 'modelo': 'Uno', 'ano': 2020, 'placa': 'ABC-1234'})

# Args e Kwargs

#Podemos passar um número indefinido de argumentos para uma função em Python. Para isso, utilizamos *args e **kwargs.

