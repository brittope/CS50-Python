def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    y = d.replace('$','')
    z = float(y)
    return z


def percent_to_float(p):
    y = p.replace('%','')
    z = float(y)
    w = z/100
    return w


main()