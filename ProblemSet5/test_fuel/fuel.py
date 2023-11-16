def main(): x = convert(input('Fraction: ')); print(gauge(x))
def convert(fraction): x1, x2 = fraction.split('/'); x1 = int(x1); x2 = int(x2); return round(x1/x2*100)
def gauge(percentage):
    if percentage < 2: return ('E')
    elif percentage >= 99: return ('F')
    else: return (f'{percentage}%')
if __name__ == "__main__": main()