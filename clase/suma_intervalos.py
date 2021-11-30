superior = int(input('Superior: '))
inferior = int(input('Inferior: '))
while inferior>superior:
    inferior = int(input(f'Introducir un numero menor que {superior}: '))
sum = 0 
count = 0
fuera_intervalo = 0
num= int(input(f'Introduce un número entre {inferior} y {superior}: '))
while num!=0:
    if num>=inferior and num<=superior:
        sum = sum+num
    else:
        fuera_intervalo = fuera_intervalo +1
    if num== inferior or num==superior:
        count= count+1
    num= int(input(f'Introduce un número entre {inferior} y {superior}: '))

print(f'La suma de los numeros entre los intervalos {inferior} y {superior} es: {sum}')
print(f'Fuera del intervalo {fuera_intervalo} numeros')
print(f'Numeros introducidos igual a los limites: {count}')