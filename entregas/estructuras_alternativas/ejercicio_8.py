nota = int(input('Nota: '))
edad = int(input('Edad: '))
sexo = input('Sexo: ')
if nota >=5 and edad >=18 and sexo=='F':
    print('ACEPTADA')
elif nota >=5 and edad >=18 and sexo=='M':
    print('POSIBLE')
else:
    print('NO ACEPTADA')