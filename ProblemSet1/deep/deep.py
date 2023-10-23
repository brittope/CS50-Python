x = input("What's the answer of life? ").lower().strip()

match x:
    case '42'|' 42 '|'forty two'|'forty-two'|'fortytwo':
        print ('yes')
    case _:
        print('no')