import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip_match = re.match(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip)
    if ip_match:
        for i in ip_match.groups():
            if not(0 <= int(i) <= 255):
                return False
        else:
            return True
    else:
        return False
if __name__ == "__main__":
    main()
