g = int(input('введите первое число'))
n = int(input('введите второе число'))
v = int(input('введите третье число'))
if g<n and g<v:
    print(g)
elif n<g and n<v:
    print(n)
elif v<g and v<n:
    print(v)
elif g==v==n:
    print('числа равны')
