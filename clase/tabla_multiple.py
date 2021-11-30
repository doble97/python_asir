lista = [int(input('Escribe un número: ')) for _ in range(2)]

for x in range(lista[0], lista[1]+1):
    for i in range(0,11):
        print(f'{x}x{i} = {x*i}')
    print('########################')