z = 0
y = 50
while y > 0:
    x = int(input('Insert a coin: '))
    match x:
        case 25:
            z = z + 25
            y = y - 25
            if z < 50:
                print(f'Amount Due: {y}')
        case 10:
            z = z + 10
            y = y - 10
            if z < 50:
                print(f'Amount Due: {y}')
        case 5:
            z = z + 5
            y = y - 5
            if z < 50:
                print(f'Amount Due: {y}')
        case _:
            if z < 50:
                print(f'Amount Due: {y}')
    if y <= 0:
        print(f'Change Owed: {z-50}')
        break