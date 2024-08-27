#conversão de tipos

# int() - converte para inteiro
# float() - converte para float
# str() - converte para string
# bool() - converte para booleano

# Exemplo de conversão de tipos

preco = 10
print(preco)
print(type(preco))

#convertendo para float

preco = float(preco)
print(preco)
print(type(preco))

preco2 = 10.50
print(preco2)
print(type(preco2))

#convertendo para int

preco2 = int(preco2)
print(preco2)
print(type(preco2))

preco3 = preco / 2

print(preco3)
print(type(preco3))

preco4 = preco // 2

print(preco4)
print(type(preco4))

novo_preco = 10.50

print(novo_preco)
print(type(novo_preco))

print(novo_preco / 2)
print(type(novo_preco / 2))
print(novo_preco // 2)
print(type(novo_preco // 2))

#convertendo para string


preco = str(preco)
print(preco)
print(type(preco))

preco2 = str(preco2)
print(preco2)
print(type(preco2))

preco3 = str(preco3)
print(preco3)
print(type(preco3))

preco4 = str(preco4)
print(preco4)
print(type(preco4))


preco_novo1 = "10.50"
print(preco_novo1)
print(type(preco_novo1))

preco_novo1 = float(preco_novo1)
print(preco_novo1)
print(type(preco_novo1))

#Onde não é possível converter para float nou int

preco_novo2 = "10.50.50"
print(preco_novo2)
print(type(preco_novo2))
preco_novo2 = float(preco_novo2)


