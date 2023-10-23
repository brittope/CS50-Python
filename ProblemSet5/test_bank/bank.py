def main():
    x = input('Digite uma saudação ')
    y = value(x)
    print(f'${y}')

def value(greeting):
    greeting = greeting.lower().strip().replace(',',' ')
    greeting_split = greeting.split()
    if greeting_split[0] == 'hello':
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
