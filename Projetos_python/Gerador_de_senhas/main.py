'''
Programador: Alex Machado Ribeiro
Programa: Gerador de senhas
Objetivo: gerar aleatoriamente uma senha segura.
'''

# NOTE: não há a necessidade de instalar pacote externo

# importa bibliteca
import secrets

while True:
    confirma = input('Deseja gerar uma senha? "s" para sim ou Enter para encerrar o programa: ')

    if confirma == 's':
        # imprime a senha gerada aleatoriamente
        print(secrets.token_urlsafe(16))
        continue
    else:
        print('Programa encerrado!')
        break