w = input('Digite uma expressão ')

k = w.split(' ')
x = float(k[0])
y = k[1]
z = float(k[2])

match y:
    case '+':
        print(round((x+z),1))
    case '-':
        print(round((x-z),1))
    case '*':
        print(round((x*z),1))
    case '/':
        print(round((x/z),1))
