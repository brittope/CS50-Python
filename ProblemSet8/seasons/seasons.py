from datetime import date
import inflect
import sys
import re
inf = inflect.engine()

def main():
    print(seasons(input('Date of Birth: ')))

def seasons(birthday):
    today = date.today()
    date_match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', birthday)

    if not date_match or today < date(*map(int, date_match.groups())):
        sys.exit('Invalid Date')

    birthdate = date(*map(int, date_match.groups()))
    x = today - birthdate
    minutes = x.total_seconds() / 60
    return conversor(int(minutes))

def conversor(minutes):
    minutes_str = inf.number_to_words(minutes, andword='')
    return (f"{minutes_str} minutes").capitalize()

if __name__ == "__main__":
    main()
