menu = {"Baja Taco": 4.00,"Burrito": 7.50,"Bowl": 8.50,"Nachos": 11.00,"Quesadilla": 8.50,"Super Burrito": 8.50,"Super Quesadilla": 9.50,"Taco": 3.00,"Tortilla Salad": 8.00};z = 0
while True:
    try:
        x = input('Item: ').title()
        if not x: break
        if x in menu: z += menu.get(x); print(f'${z:.2f}')
    except EOFError: break