# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 29 - 24/09/2024

from datetime import datetime, timedelta

tamanho_carro = ["Pequeno", "Médio", "Grande"]

tempo_lavagem_pequeno = 30
tempo_lavagem_medio = 45
tempo_lavagem_grande = 60

custo_lavagem_pequeno = 85.00
custo_lavagem_medio = 100.00
custo_lavagem_grande = 120.00

nome_lavador_pequeno = "João"
nome_lavador_medio = "José"
nome_lavador_grande = "Daniel"


def data_hora_pt_br(data_hora):
    return data_hora.strftime("%d/%m/%Y, %H:%M:%S")
#-

entrada_tamanho_carro = input("Digite o tamanho do carro: ").strip().lower()

for tamanho in tamanho_carro:
    tamanho = tamanho.lower()
    
    if entrada_tamanho_carro in tamanho:
        hora_atual = datetime.now()
        hora_fila = hora_atual + timedelta(minutes=15)

        if tamanho == "pequeno":
            print("\n")
            print("*********** LAVAR CAR DO MÁRIO ***********")
            print(f'Hora atual: {data_hora_pt_br(hora_atual)}')
            print(f'\nO seu carro é {tamanho}')
            print(f'Carro entrará na fila às: {data_hora_pt_br(hora_fila)}')
            print(f"Tempo aproximado para retirada é de: {data_hora_pt_br(hora_atual + timedelta(minutes=tempo_lavagem_pequeno))}")
            print(f"O custo da lavagem é de: R$ {custo_lavagem_pequeno:.2f}")
            print(f'Nome do Lavador é: {nome_lavador_pequeno}')
            print("******************************************")
        #--
        elif tamanho == "médio":
            print("\n")
            print("*********** LAVAR CAR DO MÁRIO ***********")
            print(f'Hora atual: {data_hora_pt_br(hora_atual)}')
            print(f'\nO seu carro é {tamanho}')
            print(f'Carro entrará na fila às: {data_hora_pt_br(hora_fila)}')
            print(f"Tempo aproximado para retirada é de: {data_hora_pt_br(hora_atual + timedelta(minutes=tempo_lavagem_medio))}")
            print(f"O custo da lavagem é de: R$ {custo_lavagem_medio:.2f}")
            print(f'Nome do Lavador é: {nome_lavador_medio}')
            print("******************************************")
        #--
        elif tamanho == "grande":
            print("\n")
            print("*********** LAVAR CAR DO MÁRIO ***********")
            print(f'Hora atual: {data_hora_pt_br(hora_atual)}')
            print(f'\nO seu carro é {tamanho}')
            print(f'Carro entrará na fila às: {data_hora_pt_br(hora_fila)}')
            print(f"Tempo aproximado para retirada é de: {data_hora_pt_br(hora_atual + timedelta(minutes=tempo_lavagem_grande))}")
            print(f"O custo da lavagem é de: R$ {custo_lavagem_grande:.2f}")
            print(f'Nome do Lavador é: {nome_lavador_grande}')
            print("******************************************")
        break
else:
    print(f'Hora atual: {data_hora_pt_br(datetime.now())}')
    print("\nTamanho não encontrado ou não disponível para lavagem no momento.")
#--
