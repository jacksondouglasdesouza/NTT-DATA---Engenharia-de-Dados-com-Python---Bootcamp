# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 19 - 18/09/2024

# FUNÇÕES

def exibir_poema(data_do_poema_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join(f'{k}: {v}' for k, v in kwargs.items())
    print(f'{data_do_poema_extenso}\n\n{texto}\n\n{meta_dados}')
#-

exibir_poema(
    "Quarta-feira, 18 de setembro de 2024",
    "O poeta é um fingidor",
    "Finge tão completamente",
    "Que chega a fingir que é dor",
    "A dor que deveras sentir.",
    autor="Jackson Douglas de Souza",
    ano=2024
)
