precio = int(input('Precio: '))
tipo = input('Tipo A o B: ')
tamanio = int(input('Tamaño 1 o 2: '))
if tipo =='A':
    if tamanio==1:
        precio = precio+0.20
    else:
        precio = precio+0.3
else:
    if tamanio==1:
        precio = precio - 0.3
    else:
        precio = precio - 0.5
print('Precio final: ', precio)