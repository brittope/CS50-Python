import validators

def main():
    print(validation(input("What's your email address? ")))

def validation(x):
    if validators.email(x):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == "__main__":
    main()
