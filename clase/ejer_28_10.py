#28/10/2021
num = int(input('Numeros a introducir: '))
numbers = [int(input('Numero: ')) for _ in range(num)]
short_numbers= 0
big_numbers = 0
neutral = 0
for x in range (len(numbers)):
    if numbers[x]>0:
        big_numbers = big_numbers+1
    elif numbers[x]<0:
        short_numbers = short_numbers+1
    else:
        neutral = neutral +1

print('Numeros mayor que 0:', big_numbers)
print('Numeros menor que 0:', short_numbers)
print('Numeros igual a 0:', neutral)