def main():
    x = input('What time is it? ')
    try:
        tfloat = convert(x)

        if  7.0 <= tfloat <= 8.0:
            print('breakfast time' )
        elif 12.0 <= tfloat <= 13.0:
            print('lunch time')
        elif 18.0 <= tfloat <= 19.0:
            print('dinner time')
    except ValueError:
        print('Error')

def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours+minutes/60

if __name__ == "__main__":
    main()