import random
x = 1

while True:
    try:
        user_lvl = int(input('Level: '))
        y = random.randint(1, user_lvl)
    except ValueError:
        True
    else:
        while x == 1:
            try:
                user_guess = int(input('Guess: '))
            except ValueError:
                x = 1
            else:
                if y > user_guess:
                    print('Too small!')
                    x = 1
                elif y < user_guess:
                    print('Too large!')
                    x = 1
                else:
                    print('Just right!')
                    x = 0
                    break
        break