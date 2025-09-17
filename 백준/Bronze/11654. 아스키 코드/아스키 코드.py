import sys

def main() -> None:
    char = sys.stdin.readline().strip()
    if not char:
        return
    print(ord(char[0]))

if __name__ == '__main__':
    main()
