'''
Programador: Alex Machado Ribeiro
Programa: Gerador de senhas
Objetivo: gerar aleatoriamente uma senha segura.
'''

# NOTE: não há a necessidade de instalar pacote externo

# importa bibliteca
import secrets

# imprime a senha gerada aleatoriamente
print(secrets.token_urlsafe(16))