import sys
lines = []

match [len(sys.argv) < 2, len(sys.argv) == 2]:
    case [False, False]:
        sys.exit ('Too many comand-line arguments')
    case [True, False]:
        sys.exit ('Too few comand-line arguments')
    case [False, True]:
        if '.py' in sys.argv[1]:
            try:
                with open(sys.argv[1]) as file:
                    for line in file:
                        if not line.strip().startswith('#') and line.strip() != '':
                            lines.append(line)
                        else:
                            pass
                    print(len(lines))
            except(FileNotFoundError):
                sys.exit ('File does not exist')
        else:
            sys.exit ('Not a python file')
