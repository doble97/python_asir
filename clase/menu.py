contactos = list()

def menu():
    print('Elija una de las siguientes opciones')
    print('1. añadir uno nuevo en el lugar indicado')
    print('2. eliminar')
    print('3. consultar')
    print('4. editar')
    print('5. listar la agenda')
    print('6. salir')
    opcion = int(input('Introduce la opcion y pulsar enter: '))
    return opcion
opcion = menu()
while opcion!=6:
    if opcion ==1:
        nombre = input('Nombre del contacto: ')
        numero = int(input('Escribe su numero: '))
        contactos.append(f'{nombre}: {numero}')
    elif opcion == 2:
        if len(contactos)>0:
            contador = 1
            for x in contactos:
                print(contador,'.',x)
                contador = contador +1
            contador = int(input('Escribe la posicion del contacto que quieras eliminar: '))
        else:
            print('No tienes contactos todavia.')
    elif opcion ==3:
        buscar = input('Escribe el numero o nombre del contacto a buscar: ')
        for x in contactos:
            if buscar in x:
                print(x)
    elif opcion == 4:
        for x in contactos:
            print(x)
        opcion = int(input('Elige un contacto para editar: '))
        contactos[opcion] = input('Escribe nombre y numero del contacto separado por espacios: ')
    elif opcion ==5:
        print('Listando usuarios: ')
        for x in contactos:
            print(x)
    print('##############################################')
    opcion = menu()