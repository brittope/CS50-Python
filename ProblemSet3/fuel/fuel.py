while True:
    frac = str(input('Fraction: ')).split('/')
    try:
        if len(frac) == 2:
            x, y = int(frac[0]), int(frac[1]); z = int(round(x/y*100))
            if x <= y:
                if z <= 2: print('E')
                elif z >= 99: print('F')
                else: print(f'{z}%')
                break
    except (ValueError, ZeroDivisionError): pass