# operadores de comparaçao (relacionais)
#  OP       SIGNIFICADO         Exemplo (true)
# >         MAIOR               2 > 1
# >=        MAIOR OU IGUAL      2 >= 2 
# <          MENOR               1 < 2
# <=        MENOR OU IGUAL      2 <= 2
# ==        IGUAL               'A' == 'A'
# !=        DIFERENTE          'A' != 'B'

maior = 2 > 1
menor = 1 < 2
maior_ou_igual = 2>= 2 
menor_ou_igual = 1<= 2
igual = 'a'== 'a'
diferente = 'a' != 'b'

linha1 = f'{maior} 2 é maior que 1, {menor} 1 é menor que 2, {maior_ou_igual} 2 é igual ou maior que 2, {menor_ou_igual} 1 é menor ou igual a 2, {igual} "A" é igual a "A", {diferente} "A" é diferente que "B"'
print (linha1)