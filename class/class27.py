# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 27 - 22/09/2024

# Aprendendo a Utilizar Dicionários em Python

# Dicionários: Criação e acesso aos dados

# Dicionários são coleções de dados que possuem chave e valor, onde os valores são acessados através das chaves
# Dicionários são mutáveis
# Dicionários são representados por chaves {}
# Dicionários não aceitam chaves duplicadas

# Criando um dicionário


pessoa_01 = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
# OU 
pessoa_02 = dict(nome="João", idade=30, cidade="São Paulo")

print(pessoa_01)
print(pessoa_02)

pessoa_01["nome02"] = "Maria"

print(pessoa_01)

#Acessando os valores de um dicionário

print(pessoa_01["nome"])
print(pessoa_01["idade"])
print(pessoa_01["cidade"])
print(pessoa_01["nome02"])

#Acessando os valores de um dicionário com o método get()

print(pessoa_01.get("nome"))
print(pessoa_01.get("idade"))
print(pessoa_01.get("cidade"))
print(pessoa_01.get("nome02"))

#Acessando as chaves de um dicionário

print(pessoa_01.keys())
print(pessoa_01.values())
print(pessoa_01.items())

# Dicionários Aninhados

contato_clientes = {
    "cliente01": {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo",
        "email": "abc@gmail.com"
    },
    "cliente02": {
        "nome": "Maria",
        "idade": 25,
        "cidade": "Rio de Janeiro",
        "email": "abc@gmail.com"
    }
}

print(contato_clientes)
print(" \n ")
# Acessando os valores de um dicionário aninhado

print(contato_clientes["cliente01"]["nome"])
print(contato_clientes["cliente01"]["idade"])
print(contato_clientes["cliente01"]["cidade"])
print(contato_clientes["cliente01"]["email"])

print(" \n ")

print(contato_clientes["cliente02"]["nome"])
print(contato_clientes["cliente02"]["idade"])
print(contato_clientes["cliente02"]["cidade"])
print(contato_clientes["cliente02"]["email"])


# Adicionando um novo item em um dicionário aninhado

contato_clientes["cliente01"]["telefone"] = "11999999999"
print(contato_clientes["cliente01"])

# Adicionando um novo item em um dicionário aninhado

contato_clientes["cliente02"]["telefone"] = "21999999999"
print(contato_clientes["cliente02"])

# Removendo um item de um dicionário aninhado

del contato_clientes["cliente01"]["email"]
print(contato_clientes["cliente01"])

# Iterando sobre um dicionário

for chave, valor in contato_clientes.items():
    print(chave)
    print(valor)
#--

print(" \n ")

for chave, valor in contato_clientes.items():
    print(f"Chave: {chave}")
    for chave2, valor2 in valor.items():
        print(f"{chave2}: {valor2}")
    print(" \n ")
#--
