fruit_cal = {'apple': 130 , 'avocado': 50 , 'banana': 110 , 'cantaloupe': 50 , 'grapefruit': 60 , 'grapes': 90 , 'honeydew_melon': 50 , 'kiwifruit': 90 , 'lemon': 15 , 'lime': 20 , 'nectarine': 60 , 'orange': 80 , 'peach': 60 , 'pear': 100 , 'pineapple': 50 , 'plums': 70 , 'strawberries': 50 , 'sweet_cherries': 100 , 'tangerine': 50 , 'watermelon': 80}
x = 0

while x == 0:
    x = str(input('Item: ')).lower().replace(' ', '_')
    if x in fruit_cal:
        y = fruit_cal.get(x)
        print(y)
        break
    else:
        break