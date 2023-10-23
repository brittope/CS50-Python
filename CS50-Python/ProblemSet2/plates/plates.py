def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    y = []
    if len(s) < 2 or len(s) > 6:
        return False
    if len(s) >= 2 and not s[:2].isalpha():
        return False
    if len(s) > 3:
        if s[-1].isalpha():
            for i in range(2,len(s)-1):
                if s[i].isdigit():
                    return False
        else:
            if s[-2].isalpha():
                for i in range(2,len(s)-2):
                    if s[i].isdigit():
                        return False
            else:
                if s[-3].isalpha():
                    for i in range(2,len(s)-3):
                        if s[i].isdigit():
                            return False
    for i in range(len(s)):
        if s[i].isdigit():
            y.append(s[i])
    if y != []:
        if y[0] == '0':
            return False
    if any(char in s for char in '. ,;:!?'):
        return False
    return True
main()