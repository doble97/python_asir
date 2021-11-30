#Primero creamos una función que solo imprima el menú
def ingredientes()->None:
    print('Elige ingredientes (al lado sale su presio) o pulsa 0 para salir: ')
    print('1. York 1€')
    print('2. Bacon 2€')
    print('3. Pepperoni 1€')
    print('4. Champiñón 1€')
    print('5. Cebolla 1€')
    print('6. Piña 2€')
    print('7. Pepinillo 1€')
    print('8. Aceitunas negras 1.5€')
    print('9. Tomate 2€')
    print('10. Rúcula 1€')
    print('11. Queso 1€')
    print('12. Queso cheddar 1.5€')
    print('13. 5 Quesos 3€')
def elegir_ingredientes(opcion:int)->float:
    lista = [1,2,1,1,1,2,1,1.5,2,1,1,1.5,3]
    return lista[opcion-1]

def add_ingredientes():
    factura = 0
    ingredientes()
    opcion = int(input("Opción"))
    if opcion==0:
        print("Salir")
    else:
        factura = elegir_ingredientes(opcion)
        ingredientes()
        opcion = int(input('Opcion: '))
        while opcion !=0 and opcion < 14:
            factura = factura + elegir_ingredientes(opcion)
            #ingredientes()
            opcion = int(input('Opcion: '))
    return factura
costo_total = add_ingredientes()
print('Factura total: ', costo_total)
