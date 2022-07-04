g = int(input('введите год'))
if g % 4 == 0 and g % 100 != 0 and g % 400 == 0:
    print('yes')
else:
    print('no')
