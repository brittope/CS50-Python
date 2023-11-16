names = []
while True:
    try:
        name = input("What's your name? ")
        names.append(name)
    except(EOFError):
        print(names)
        break
