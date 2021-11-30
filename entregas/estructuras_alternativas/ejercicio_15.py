alumnos = int(input('Numero de alumnos: '))
if alumnos>=100:
    print('En total se pagará', alumnos*65, '€')
    print('Cada alumno pagará',65,'€')
elif  alumnos>=50 and alumnos<=99:
    print('En total se pagará', alumnos*70, '€')
    print('Cada alumno pagará',70,'€')
elif alumnos >=30 and alumnos<=49:
    print('En total se pagará', alumnos*95, '€')
    print('Cada alumno pagará',95,'€')
else:
    print('En total se pagará', 4000, '€')
    print('Cada alumno pagará',4000/alumnos,'€')