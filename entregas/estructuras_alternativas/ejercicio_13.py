day = int(input('DÍA: '))
month = int(input('MES: '))
year = int(input('AÑO: '))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and year <= 2021:
    if day > 0 and day <= 31:
        print('Formato de fecha correcta')
elif month == 4 or month == 6 or month == 9 or month == 11 and year<=2021:
    if day > 0 and day <= 30:
        print('Formato de fecha correcta')
elif month == 2 and day==29:
    if year/4 == int(year/4) and year/100 != int(year/100) and year/400 == int(year/400):
        print('Formato de fecha correcta')
else:
    if day<=28:
        print('Formato de fecha correcta')