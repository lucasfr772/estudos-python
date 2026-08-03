# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condiçoes prencisam ser
# VERDADEIRAS
# Se qualquer valor for considerado falso,
# a expressao inteira será avaliada naquele valor
# São consideradas falsy (que vc já viu)
# 0 0.0 '' False
# Também existe p tipo None que é 
# usado para representar um não valor

entrada= input ('[E]ntrar [S]air: ')
senha_digitada = input('senha:')

senha_permitida = '12345'
if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida or senha_digitada != senha_permitida:
    print('entrar')
    print('senha incorreta')
else:
    print('sair')


#avaliação de curto circuito
#print(True and False and True)



