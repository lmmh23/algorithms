import sys

def main() -> None:
    data = sys.stdin.readline().strip().split()
    if len(data) != 2:
        return
    number, base = data[0], int(data[1])
    value = 0
    for ch in number:
        if '0' <= ch <= '9':
            digit = ord(ch) - ord('0')
        else:
            digit = ord(ch) - ord('A') + 10
        value = value * base + digit
    print(value)

if __name__ == '__main__':
    main()
