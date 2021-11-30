caracter = input('Escribe un caracter: ')

while caracter and caracter !=" ":
    if caracter in "aeiou":
        print('Vocal')
    else:
        print('No vocal')
    caracter = input('Introduce un caracter: ')