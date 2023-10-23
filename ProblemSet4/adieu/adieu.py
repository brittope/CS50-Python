import inflect
p = inflect.engine()
names = []

while True:
    try:
        x = input('Name: ')
        names.append(x)
    except EOFError:
        print(f'Adieu, adieu, to {p.join(names)}')
        break