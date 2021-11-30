minutos = int(input('Número de minutos: '))
horas = int(minutos/60)
min = ((minutos/60)-horas) *60
print(f'{minutos} minutos son --> {horas} horas y {min} minutos')