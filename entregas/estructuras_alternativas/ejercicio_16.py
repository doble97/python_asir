minutos = int(input('Minutos hablados: '))
costo = 0
if minutos>10:
    costo = 5*1+3*0.8+2*0.7+(minutos-10)*0.5
elif minutos <= 5:
    costo = minutos
elif minutos >=6 and minutos<=8:
    costo = 5+(minutos-5)*0.8
else:
    costo = 5+(minutos-5)*0.8+ (minutos-8)*0.7

print('Gasto total', costo, '€')