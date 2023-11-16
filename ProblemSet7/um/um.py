import re

def main():
    print(count(input("Text: ")))

def count(s):
    if matches := re.findall(r'\b[Uu]m\b', s):
        return len(matches)

if __name__ == "__main__":
    main()
