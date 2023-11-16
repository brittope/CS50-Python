import requests; import sys
try:
    if len(sys.argv) == 2:
        try: x = float(sys.argv[1]); y = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json'); z = y.json(); print("${:,.4f}".format(x * z['bpi']['USD']['rate_float']))
        except requests.RequestException: print('ERROR'); sys.exit()
    else: sys.exit('Missing')
except ValueError: sys.exit('Command-line argument is not a number')