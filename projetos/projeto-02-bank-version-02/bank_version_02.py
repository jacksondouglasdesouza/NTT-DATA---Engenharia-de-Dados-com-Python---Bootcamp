from datetime import datetime, timedelta
import pytz

# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 31 - 24/09/2024

# Criando um Sistema Bancário com Python - Versão 02

fuso_brasil = pytz.timezone('America/Sao_Paulo')

def obter_data_hora():
    data_hora_atual = datetime.now(fuso_brasil)
    return data_hora_atual.strftime("%d/%m/%Y, %H:%M:%S")
#--

opcao_servico_bancario = f"""

**********************************************************
**********************************************************
****    BANCO NTT DATA                                ****
****    São Paulo - {obter_data_hora()}              ****
****    Escolha o serviço bancário desejado:          ****
****    Depositar [d]                                 ****
****    Sacar [s]                                     ****
****    Extrato [e]                                   ****
****    Sair [x]                                      ****
**********************************************************
**********************************************************
"""
#--

saldo = 0
LIMITE = 500
extrato = []
numero_transacoes_diarias = 0
LIMITE_TRANSACOES_DIARIAS = 10

while True:
    
    VALUE_ENTRADA = input(opcao_servico_bancario).lower().strip()
    
    data_hora_atual = obter_data_hora()

    if numero_transacoes_diarias >= LIMITE_TRANSACOES_DIARIAS:
        if VALUE_ENTRADA in ['d', 's']:
            print("Operação não permitida: você atingiu o limite de transações diárias.")
            continue
        #--
    #--

    if VALUE_ENTRADA == 'd':
        valor_deposito = float(input('Digite o valor do depósito: '))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f'Operação de Depósito de [ + R$ {valor_deposito:.2f} ] - {data_hora_atual}')
            numero_transacoes_diarias += 1
            print(f'Depósito de R$ {valor_deposito:.2f} foi realizado com sucesso!')
        else:
            print('Depósito inválido! O valor deve ser maior que zero.')
        #--
    #--

    elif VALUE_ENTRADA == 's':
        valor_saque = float(input('Digite o valor do saque: '))
        
        if valor_saque > 0:
            if valor_saque <= LIMITE:
                if saldo >= valor_saque:
                    saldo -= valor_saque
                    extrato.append(f'Operação de Saque de [ - R$ {valor_saque:.2f} ] - {data_hora_atual}')
                    numero_transacoes_diarias += 1
                    print(f'Saque de R$ {valor_saque:.2f} foi realizado com sucesso!')
                else:
                    print('Saldo insuficiente!')
            else:
                print('Limite de saque ultrapassado! Só é permitido saque de até R$ 500,00.')
        else:
            print('Saque inválido! O valor deve ser maior que zero.')
        #--
    #--

    elif VALUE_ENTRADA == 'e':
        print(f"###############################################################\n")
        print(f"##############  BANCO NTT DATA EXTRATO BANCÁRIO  ##############\n")
        print(f"####           São Paulo - {data_hora_atual}             ###\n")
        print(f"###############################################################\n")
        
        if extrato:
            for transacao in extrato:
                print(transacao)
            #--
            print(f'Saldo atual: R$ {saldo:.2f}\n')
            print(f"###############################################################\n")
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