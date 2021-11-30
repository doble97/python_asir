a = int(input('Número: '))
b = int(input('Número: '))
c = int(input('Número: '))
if a>b and a>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b>a and b>c:
    if a>c:
        print(b,a,c)
    else:
        print(b,c,b)
else:
    if a>b:
        print(c,a,b)
    else:  
        print(c,b,a)