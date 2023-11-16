import sys
import csv

def check_sys():
    match [len(sys.argv) < 3, len(sys.argv) == 3]:
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
header = ['first, last, house']
students = []

if check_sys() is True:
    with open(sys.argv[1]) as file:
        rows = csv.DictReader(file)
        for line in file  :
            line = line.replace('"', '').replace('\n', '').replace(' ', '')
            lines.append(line.split(","))
        for _ in range(1, len(lines)):
            students.append({'first':lines[_][1], 'last':lines[_][0], 'house':lines[_][2]})
    with open (sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first','last','house'])
        writer.writeheader()
        writer.writerows(students)
