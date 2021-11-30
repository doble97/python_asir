left_number = int(input('Escribe numero inicial: '))
right_number = int(input('Escribe numero último: '))
count = left_number
for x in range(left_number, right_number+1):
    if x%2==0:
        print(x)