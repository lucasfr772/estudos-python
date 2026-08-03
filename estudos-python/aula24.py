# Operadores in e not in
# Strings são interáveis
# 0 1 2 3 4 5 
# O T A V I O
# -6 -5 -4 -3 -2 -1
nome = input('digite o seu nome: ')
encontrar = input('digite o que voce quer encontrar: ')

if encontrar in nome:
    print(f'`{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')