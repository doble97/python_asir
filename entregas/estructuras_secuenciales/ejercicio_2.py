def ejercicio2():
    base = int(input('Base: '))
    altura = int(input('Altura: '))
    area = (base*altura)/2
    #altura= c^2 + c^2
    cateto = (altura**2 - base**2)**(1/2)






def ejercicio10():
    num1= int(input('Número 1: '))
    num2= int(input('Número 2: '))
    distancia = num1-num2 if (num1-num2)>=0 else (num1-num2)*-1
    print('La distancia es: ', distancia)