def main():
    x = input('Fraction: ')
    y = convert(x)
    print(gauge(y))

def convert(fraction):
    x1, x2 = fraction.split('/')
    x1 = int(x1)
    x2 = int(x2)
    x3 = round(x1/x2*100)
    return x3

def gauge(percentage):
    if percentage < 2:
        return ('E')
    elif percentage >= 99:
        return ('F')
    else:
        return (f'{percentage}%')

if __name__ == "__main__":
    main()