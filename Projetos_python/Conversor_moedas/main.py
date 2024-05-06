'''
Programador: Alex Machado Ribeiro
Programa: Conversor de moedas
Objetivo: converter o valor de uma moeda de um país para outro, de acordo com a cotação do dia.
'''

# NOTE: precisa instalar o pacote forex: pip install forex-python

# importa a biblioteca de conversão de valores que contém a cotação atual de várias moedas
from forex_python.converter import CurrencyRates

while True:
    # variáveis e entrada de dados
    valor = str(input('Informe o valor a ser convertido ou Enter para encerrar o programa: ')).replace(',','.') # recebe string e converte vírgula para ponto

    if valor != '':
        valor = float(valor) # converte string para ponto flutuante
        moeda_origem = input('Digite a moeda de origem (exemplo: USD, EUR, BRL): ').upper() # recebe a moeda de origem desejada e converte para caixa alta
        moeda_destino = input('Digite a moeda de destino (exemplo: USD, EUR, BRL): ').upper() # recebe a moeda de destino desejada e converte para caixa alta

        try:
            # faz a conversão
            resultado = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

            # exibe o resultado na tela
            print(f'$ {valor:,.2f} {moeda_origem} = $ {resultado:,.2f} {moeda_destino}.')
        except:
            print('Não foi possível fazer a conversão.')
        finally:
            continue
    else:
        print('Programa encerrado.')
        break