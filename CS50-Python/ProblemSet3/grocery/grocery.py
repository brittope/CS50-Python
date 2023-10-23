groceries = []

while True:
    try:
        x = input().upper()
        groceries.append(x)
    except EOFError:
            groceries_single = set(groceries)
            for i in sorted(groceries_single):
                y = groceries.count(i)
                print(f'{y} {i}')
            break