from datetime import datetime
import pytz

fuso_brasil = pytz.timezone('America/Sao_Paulo')

def obter_data_hora():  # Função para obter data e hora local pt_br
    data_hora_atual = datetime.now(fuso_brasil)
    return data_hora_atual.strftime("%d/%m/%Y, %H:%M:%S")

def normalizar_cpf(cpf):  # Função para normalizar CPF - remover espaços e pontos
    return cpf.replace(".", "").replace("-", "").strip()

def validar_cpf(cpf):  # Função para validar CPF - verifica se tem 11 dígitos
    return cpf.isdigit() and len(cpf) == 11

def validar_valor(valor):  # Função para validar valor - verifica se é numérico e maior que zero
    if isinstance(valor, (int, float)) and valor > 0:
        return True
    elif isinstance(valor, str) and valor.replace('.', '', 1).isdigit():
        return float(valor) > 0
    return False

def cadastrar_cliente(clientes, nome, data_nascimento, cpf, endereco):  # Cadastro de cliente e criação de conta
    cpf = normalizar_cpf(cpf)
    if not validar_cpf(cpf):
        print(f"Erro: CPF {cpf} inválido. Insira um CPF válido de 11 dígitos.")
        return
    if cpf in [cliente['cpf'] for cliente in clientes]:
        print(f"Erro: CPF {cpf} já cadastrado.")
        return
    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
        'contas': [],
        'transacoes_diarias': 0  # Controle de transações diárias
    }
    clientes.append(cliente)
    criar_conta_bancaria(cliente)

def criar_conta_bancaria(cliente):  # Função para criar conta bancária
    numero_conta = f"{len(cliente['contas']) + 1:03d}"
    nova_conta = {
        'agencia': "0001",
        'numero_conta': numero_conta,
        'saldo': 0,
        'extrato': [],
        'transacoes_diarias': 0  # Controle de transações diárias por conta
    }
    cliente['contas'].append(nova_conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

def cancelar_conta(clientes, cliente, numero_conta):  # Cancelar conta e excluir cliente se necessário
    contas = cliente['contas']
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            contas.remove(conta)
            print(f"Conta {numero_conta} cancelada com sucesso!")
            break
    if len(contas) == 0:
        clientes.remove(cliente)
        print(f"Cliente {cliente['nome']} removido do sistema.")

def listar_contas(cliente):  # Listar contas vinculadas a um cliente
    print(f"Contas do cliente {cliente['nome']}:")
    for conta in cliente['contas']:
        print(f"Conta {conta['numero_conta']} - Agência: {conta['agencia']} - Saldo: R$ {conta['saldo']:.2f}")

def verificar_cliente_possui_conta(clientes, cpf):  # Verificar se o cliente possui conta
    cpf = normalizar_cpf(cpf)
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print(f"O cliente {cliente['nome']} possui contas no banco.")
            return cliente
    print(f"Nenhum cliente com o CPF {cpf} encontrado.")
    return None

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # Função de saque
    if valor <= 0:
        print("Saque inválido. O valor deve ser maior que zero.")
        return saldo, extrato
    if valor > limite:
        print(f"Erro: Limite de saque de R$ {limite:.2f} excedido.")
        return saldo, extrato
    if saldo < valor:
        print("Erro: Saldo insuficiente.")
        return saldo, extrato
    if numero_saques >= limite_saques:
        print("Erro: Limite de saques diários excedido.")
        return saldo, extrato

    saldo -= valor
    extrato.append(f"Saque de R$ {valor:.2f} realizado em {obter_data_hora()}")
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

def depositar(saldo, valor, extrato, /):  # Função de depósito
    if valor <= 0:
        print("Depósito inválido. O valor deve ser maior que zero.")
        return saldo, extrato
    saldo += valor
    extrato.append(f"Depósito de R$ {valor:.2f} realizado em {obter_data_hora()}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):  # Função Extrato
    print("\n################# EXTRATO BANCÁRIO #################")
    if extrato:
        for transacao in extrato:
            print(transacao)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("###################################################\n")

def menu_bancario():  # Função do menu - sistema bancário
    opcao_servico_bancario = f"""
    **********************************************************
    ****    BANCO NTT DATA                                ****
    ****    São Paulo - {obter_data_hora()}              ****
    ****    Escolha o serviço bancário desejado:          ****
    ****    [nc] Novo Cliente                             ****
    ****    [lc] Listar Contas de um Cliente              ****
    ****    [cc] Cancelar Conta                           ****
    ****    [s] Sacar                                     ****
    ****    [d] Depositar                                 ****
    ****    [e] Exibir Extrato                            ****
    ****    [x] Sair                                      ****
    **********************************************************
    """
    
    clientes = []
    limite_saque_diario = 500
    limite_transacoes_diarias = 10

    while True:
        escolha = input(opcao_servico_bancario).lower().strip()

        if escolha == 'nc':  # Novo cliente e conta
            nome = input("Digite o nome do cliente: ")
            data_nascimento = input("Digite a data de nascimento no formato (dd/mm/yyyy): ")
            cpf = input("Digite o CPF (apenas números): ")
            endereco = input("Digite o endereço (logradouro, número - bairro - cidade/UF): ")
            cadastrar_cliente(clientes, nome, data_nascimento, cpf, endereco)

        elif escolha == 'lc':  # Listar contas do cliente
            cpf = input("Digite o CPF para listar as contas: ")
            cliente = verificar_cliente_possui_conta(clientes, cpf)
            if cliente:
                listar_contas(cliente)

        elif escolha == 'cc':  # Cancelar conta
            cpf = input("Digite o CPF do cliente que deseja cancelar a conta: ")
            cliente = verificar_cliente_possui_conta(clientes, cpf)
            if cliente:
                listar_contas(cliente)
                numero_conta = input("Digite o número da conta que deseja cancelar: ")
                cancelar_conta(clientes, cliente, numero_conta)

        elif escolha == 's':  # Saque
            cpf = input("Digite o CPF para realizar o saque: ")
            cliente = verificar_cliente_possui_conta(clientes, cpf)
            if cliente:
                listar_contas(cliente)
                numero_conta = input("Digite o número da conta para saque: ")
                for conta in cliente['contas']:
                    if conta['numero_conta'] == numero_conta:
                        valor_saque = input("Digite o valor do saque: ")
                        if validar_valor(valor_saque):
                            valor_saque = float(valor_saque)
                            conta['saldo'], conta['extrato'] = sacar(
                                saldo=conta['saldo'], valor=valor_saque, extrato=conta['extrato'],
                                limite=limite_saque_diario, numero_saques=len(conta['extrato']),
                                limite_saques=limite_transacoes_diarias
                            )

        elif escolha == 'd':  # Depósito
            cpf = input("Digite o CPF para realizar o depósito: ")
            cliente = verificar_cliente_possui_conta(clientes, cpf)
            if cliente:
                listar_contas(cliente)
                numero_conta = input("Digite o número da conta para depósito: ")
                for conta in cliente['contas']:
                    if conta['numero_conta'] == numero_conta:
                        valor_deposito = input("Digite o valor do depósito: ")
                        if validar_valor(valor_deposito):
                            valor_deposito = float(valor_deposito)
                            conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor_deposito, conta['extrato'])

        elif escolha == 'e':  # Extrato
            cpf = input("Digite o CPF para exibir o extrato: ")
            cliente = verificar_cliente_possui_conta(clientes, cpf)
            if cliente:
                listar_contas(cliente)
                numero_conta = input("Digite o número da conta para exibir o extrato: ")
                for conta in cliente['contas']:
                    if conta['numero_conta'] == numero_conta:
                        exibir_extrato(conta['saldo'], extrato=conta['extrato'])

        elif escolha == 'x':  # Sair do sistema
            print("Saindo do sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_bancario()


# - OBSERVAÇÕES PARA FAZER AMANHÃ:
    # - 1 - Ao validar o CPF na conta e o cliente tendo conta, não perguntar o CPF novamente, pois, quando na primeira validação,
    # o cliente acessa a coo, ele está dentro da conta e pode fazer todas as operações sem precisar novamente
    # validar o CPF em cada operação.
    # - 1.1 - Caso o cliente possua 2 ou mais contas, na validação o cliente vai escolher qual conta quer acessar e a partir daí, após
    # está validado certinho e escolhido qual conta quer acessar, ele pode fazer todas as operações sem precisar novamente validar
    # o CPF em cada operação.
    
    # - 2 - Ao escolher cadastrar um novo cliente, estando dentro da logado dentro de uma conta, não é possível cadastrar outro cliente,
    # pois o cliente não é um novo clliente, ele já é um cliente e está logado dentro de uma conta. Ao está logado dentro de uma conta,
    # o certo a fazer é dar a opção de cadastrar uma nova conta para o cliente logado. Ou seja, uma mensagem de erro deve ser exibida
    # caso o cliente tente cadastrar um novo cliente estando logado dentro de uma conta. A mensagem de erro deve ser algo do tipo:
    # "Erro: Você já é um cliente e está logado dentro de uma conta.
    
    # - PENSAR EM MAIS COISAS PARA FAZER AMANHÃ... VOU DORMIR AGORA... ATÉ AMANHÃ... FUI... VLW, FLW... #partiu... #boanoite... #semdormir...
    # KKKKKKKKKKKKK
    # - FUI... #partiu... "boa noite" 07:31 AM... K
    # Mano do céu... K tou locão falando comigo mesmo... K
    # kkkkkkkkkkkkkk
