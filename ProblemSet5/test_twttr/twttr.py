def main():
    tweet = input('What is happening?! ')
    print(shorten(tweet))

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    y = [letter for letter in word if letter.lower() not in vowels]
    y = ''.join(y)
    return y

if __name__ == "__main__":
    main()