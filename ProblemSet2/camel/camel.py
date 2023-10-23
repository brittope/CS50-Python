import re
snake=''

x = input('Digite o nome de uma variável em camel case ')
y = re.findall('.[^A-Z]*', x)
for i in range(len(y)-1):
    snake = snake+y[i]+'_'

snake2 = snake+y[-1]
z = snake2.lower()
print(z)