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