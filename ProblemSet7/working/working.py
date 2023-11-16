import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r'^(\d+):?([\d][\d])? (AM|PM) to (\d+):?([\d][\d])? (AM|PM)$', s):
        duration = matches.groups()
    else:
        raise ValueError

    if int(duration[0]) > 12 or int(duration[3]) > 12:
        raise ValueError
    if duration[1] and int(duration[1]) >= 60 or duration[4] and int(duration[4]) >= 60:
        raise ValueError

    if duration[1]: min1 = duration[1]
    else: min1 = '00'
    if duration[4]: min2 = duration[4]
    else: min2 = '00'

    if int(duration[0]) == 12 and duration[2] == 'AM':
        x = '00:' + min1
    elif 1 <= int(duration[0]) <= 11 and duration[2] == 'PM':
        x = f'{int(duration[0]) + 12}' + ':' + min1
    else:
        x = f'{int(duration[0]):02}' + ':' + min1
    if int(duration[3]) == 12 and duration[5] == 'AM':
        y = '00:' + min2
    elif 1 <= int(duration[3]) <= 11 and duration[5] == 'PM':
        y = f'{int(duration[3]) + 12}' + ':' + min2
    else:
        y = f'{int(duration[3]):02}' + ':' + min2

    return x + ' to ' + y

if __name__ == "__main__":
    main()
