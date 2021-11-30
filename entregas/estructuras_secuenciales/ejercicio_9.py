#1. 55% del promedio de sus calificaciones parciales
#2. 30% de la calificación de sus trabajos
#3. 15% calificación examen final
parciales = float(input('Nota de los parciales: '))
trabajos = float(input('Nota de los trabajos: '))
examen = float(input('Exámen: '))
nota_total = parciales*0.55+ trabajos*0.3+examen*0.15
print('Nota final: ', nota_total)