def convert (x):
    if ":)" in x and ":(" in x:
        y = (x.replace(':)', '🙂'))
        return print(y.replace(':(', '🙁'))
    elif ":)" in x:
        return print(x.replace(':)', '🙂'))
    elif ":(" in x:
        return print(x.replace(':(', '🙁'))


def main ():
    phrase = str(input('Digite uma frase contendo ":)" ou ":("'))
    convert(phrase)

main ()