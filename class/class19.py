# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 19 - 01/09/2024

'''
String múltiplas linhas
Manipulando Strings com Python

'''

nome_usuario_completo = 'Jackson Douglas de Souza'
idade_usuario = 45
endereco_usuario = 'Rua das Flores, 12307, Bairro de Flores - Manaus - AM'
email_usuario = 'email@proton.me'
telefone_usuario = '(92) 99999-9999'
cpf_usuario = '123.456.789-10'
rg_usuario = '1234567'
data_nascimento_usuario = '01/01/1979'
nome_mae_usuario = 'Maria da Silva'
nome_pai_usuario = 'José da Silva'

mensagem_informativa = f'''
    Boa noite, {nome_usuario_completo}!
    Venho através deste e-mail informar que sua conta foi bloqueada por motivos de segurança.
    Por favor, entre em contato com o suporte para mais informações.
    Confimação de dados do usuário:
    - Nome: {nome_usuario_completo}
    - Idade: {idade_usuario}
    - Endereço: {endereco_usuario}
    - E-mail: {email_usuario}
    - Telefone: {telefone_usuario}
    - CPF: {cpf_usuario}
    - RG: {rg_usuario}
    - Data de nascimento: {data_nascimento_usuario}
    - Nome da mãe: {nome_mae_usuario}
    - Nome do pai: {nome_pai_usuario}
    Confirme os seus dados entrar em contato com o suporte.
    Assim poderemos liberar o seu acesso.
    Obrigado!
    Jackson Douglas de Souza
    Assistente de Suporte
'''

print(mensagem_informativa)