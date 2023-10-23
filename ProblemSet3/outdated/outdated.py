import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input('Date: ').strip()
    date_match = re.match(r'(\d{1,2})/(\d{1,2})/(\d{4})$', date)
    if date_match:
        m, d, y = [int(part) for part in date_match.groups()]
        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f'{y:04d}-{m:02d}-{d:02d}')
            break
    else:
        date_parts = date.capitalize().split()
        if len(date_parts) == 3 and date_parts[0] in months and date_parts[1].endswith(','):
            m = months.index(date_parts[0]) + 1
            d = int(date_parts[1].rstrip(','))
            y = int(date_parts[-1])
            if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f'{y:04d}-{m:02d}-{d:02d}')
                    break
            else:
               True