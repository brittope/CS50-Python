def vow_del(x):
    vowels = ['a', 'e', 'i', 'o', 'u']

    y = [letter for letter in x if letter.lower() not in vowels]
    y = ''.join(y)
    print(y)

tweet = str(input('What is happening?! '))
vow_del(tweet)