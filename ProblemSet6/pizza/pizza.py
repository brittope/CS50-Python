import sys
from tabulate import tabulate

def check_sys():
    match [len(sys.argv) < 2, len(sys.argv) == 2]:
        case [False, False]:
            sys.exit ('Too many comand-line arguments')
        case [True, False]:
            sys.exit ('Too few comand-line arguments')
        case [False, True]:
            if '.csv' in sys.argv[1]:
                    try:
                        with open(sys.argv[1]) as file:
                            return True
                    except (FileNotFoundError):
                        sys.exit("File does not exist")
            else:
                sys.exit("Not a CSV file")

lines = []

if check_sys() is True:
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.replace('\n','')
            lines.append(line.split(','))
            print(tabulate(lines, headers='firstrow', tablefmt='grid'))
