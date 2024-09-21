# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 23 - 21/09/2024

# Criando um Sistema Bancário com Python - Versão 01

opcao_servico_bancario = """
    Banco NTT DATA\n
    Escolha o serviço bancário desejado:
    Depositar [d]
    Sacar [s]
    Extrato [e]
    Sair [x]
"""

saldo = 0
LIMITE = 500
extrato = []
numero_saques_diarios = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    
    VALUE_ENTRADA = input(opcao_servico_bancario).lower().strip()
    
    if VALUE_ENTRADA == 'd':
        valor_deposito = float(input('Digite o valor do depósito: '))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f'Depósito de [ + R$ {valor_deposito:.2f} ]')
            print(f'Depósito de R$ {valor_deposito:.2f} foi realizado com sucesso!')
        else:
            print('Depósito inválido! O valor deve ser maior que zero.')
    #--
    
    elif VALUE_ENTRADA == 's':
        valor_saque = float(input('Digite o valor do saque: '))
        
        if valor_saque > 0:
            if numero_saques_diarios < LIMITE_SAQUES_DIARIOS:
                if valor_saque <= LIMITE:
                    if saldo >= valor_saque:
                        saldo -= valor_saque
                        extrato.append(f'Saque de [ - R$ {valor_saque:.2f} ]')
                        numero_saques_diarios += 1
                        print(f'Saque de R$ {valor_saque:.2f} foi realizado com sucesso!')
                    else:
                        print('Saldo insuficiente!')
                else:
                    print('Limite de saque ultrapassado! Só é permitido saque de até R$ 500,00.')
            else:
                print('Limite de saques diários atingido!')
        else:
            print('Saque inválido! O valor deve ser maior que zero.')
        #--
    #--
    
    elif VALUE_ENTRADA == 'e':
        print("********************")
        print(f'\nExtrato bancário:')
        if extrato:
            for transacao in extrato:
                print(transacao)
            #--
            print(f'Saldo atual: R$ {saldo:.2f}\n')
        else:
            print("Nenhuma movimentação registrada.")
            print(f'Saldo atual: R$ {saldo:.2f}\n')
        #--
    #--
    
    elif VALUE_ENTRADA == 'x':
        print('Sessão finalizada!')
        break
    #--
    
    else:
        print(f'Operação inválida. Valor digitado foi [ {VALUE_ENTRADA} ].')
        print('Digite uma opção válida: d, s, e ou x.')
    #--
    
#-- end while
