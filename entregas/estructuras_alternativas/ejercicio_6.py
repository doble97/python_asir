word = input('Escribe una palabra: ')
for x in word:
    if x.isupper():
        print('Hay una letra en mayúscula')
        break