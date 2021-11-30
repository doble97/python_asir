cuenta = 0


def tam_pizza() -> int:
    price_tam = [8, 10, 12]
    print('Escribe el numero de la opción de tamaño: ')
    print("1. Individual")
    print("2. Mediano")
    print("3. Familiar")
    elegir = int(input('Tu opcion: '))
    return price_tam[elegir-1]


def tipo_masa() -> float:
    price = [1, 0.5]
    print('Elije tipo de masa: ')
    print('1. Fina')
    print('2. Clásica')
    opcion = int(input('Opcion: '))
    return price[opcion-1]


def ingredientes() -> None:
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


def elegir_ingredientes(opcion: int) -> float:
    lista = [1, 2, 1, 1, 1, 2, 1, 1.5, 2, 1, 1, 1.5, 3]
    return lista[opcion-1]


def validar_ingredientes(opcion) -> bool:
    return opcion != 0 and opcion < 14


def preguntar_ingredientes() -> int:
    ingredientes()
    opcion = int(input("Opción: "))

def add_ingredientes()->float:
    factura = 0
    opcion = preguntar_ingredientes()
    if opcion==0:
        print("Salir")
    else:
        factura = elegir_ingredientes(opcion)
        opcion = preguntar_ingredientes()
        while validar_ingredientes(opcion):
            factura = factura + elegir_ingredientes(opcion)
            opcion = preguntar_ingredientes()
    return factura

cuenta = tam_pizza()
cuenta = cuenta + tipo_masa()
cuenta = cuenta + add_ingredientes()
print('Tu cuenta total es:', cuenta)