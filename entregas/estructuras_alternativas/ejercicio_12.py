year = int(input('AÑO: '))
if year/4 == int(year/4) and year/100 != int(year/100) and year/400 == int(year/400):
    print(year, 'es bisiesto')
else:
    print(year, 'no es bisiesto')
