base = int(input('Base: '))
exponente = int(input('Exponente'))
if exponente > 0:
    print('Potencia:', base**exponente)
elif exponente<0:
    print('Potencia:', 1/(base**exponente))
else:
    print('Potencia: 1')