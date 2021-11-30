A = int(input('LADO A:'))
B = int(input('LADO B:'))
C = int(input('LADO C:'))
pitagoras = (B**2+C**2)**(1/2)
if A==pitagoras:
    print('Triangulo rectángulo')
elif A==B and B==C:
    print('Triángulo equilátero')
elif A==B or B==C or C==A:
    print('Triángulo isósceles')
else:
    print('Triángulo escaleno')