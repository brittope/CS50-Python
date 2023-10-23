import random

def main():
    score = 0
    x = get_level()
    for i in range(10):
        p1 = generate_integer(x)
        p2 = generate_integer(x)
        ans = p1 + p2
        for _ in range(3):
            user_ans = int(input(f'{p1} + {p2} = '))
            if user_ans == ans:
                break
            else:
                print('EEE')
        else:
            print(f'{p1} + {p2} = {ans}')
            score += 1
    else:
        print('Score:',10-score)

def get_level():
    while True:
        try:
            x = int(input('Level: '))
            if x > 3 or x < 1:
                pass
            else:
                return x

        except ValueError:
            pass

def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            pass

if __name__ == "__main__":
    main()