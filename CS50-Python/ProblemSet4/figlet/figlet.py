import sys
import random
from pyfiglet import Figlet

def main():
    if len(sys.argv) == 1:
        font_n = random.choice(Figlet().getfonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '-font'):
        font_n = sys.argv[2]
    else:
        sys.exit("Usage: figlet.py [-f/--font FONT_NAME]")

    figlet = Figlet(font=font_n)
    u_input = input('Enter text: ')
    print(figlet.renderText(u_input))

if __name__ == '__main__':
    main()