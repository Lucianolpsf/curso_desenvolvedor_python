# importa bibliotecas de data e calendário
import calendar
from datetime import date

# informa o dia, mês e ano atual
dia = date.today().day
mes_atual = date.today().month
ano = date.today().year

# imrpime a data atual e o título do programa
print(f'Data atual: {dia}/{mes_atual}/{ano}.')
print(f'\nCalendário:\n')

# exibe o calendário de cada mês do ano atual
for mes in range(12):
    print(calendar.month(ano, mes + 1))