# NTT DATA BOOTCAMP - Engenharia de Dados com Python
# Aula 30 - 24/09/2024

# Trabalhando com timezone

from datetime import datetime, timedelta
import pytz

# Criando um objeto timezone

timezone_brasil = datetime.now(pytz.timezone('America/Sao_Paulo'))
timezone_africa = datetime.now(pytz.timezone('Africa/Asmera'))
timezone_bucharest = datetime.now(pytz.timezone('Europe/Bucharest'))
timedelta_canada = datetime.now(pytz.timezone('Canada/Central'))

print(f'Horário de Brasília: {timezone_brasil}')
print(f'Horário de Asmara: {timezone_africa}')
print(F'Horário de Bucareste: {timezone_bucharest}')
print(f'Horário de Toronto: {timedelta_canada}')

#--------------------------------------------

