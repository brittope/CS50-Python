x = str(input('Digite uma saudação ').lower().strip().replace(',',' '))

y = x.split()
if y[0] == 'hello':
    print('$0')
elif x.startswith('h'):
    print('$20')
else:
    print('$100')

