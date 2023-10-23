import requests
import sys

try:
    if len(sys.argv) == 2:
        x = float(sys.argv[1])
        try:
            y = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            z = y.json()
            w = z['bpi']['USD']['rate_float']
            total = x * w
            f_total = "${:,.4f}".format(total)
            print(f_total)
        except requests.RequestException:
            print('ERROR')
            sys.exit()
    else:
        sys.exit('Missing')
except ValueError:
    sys.exit('Command-line argument is not a number')