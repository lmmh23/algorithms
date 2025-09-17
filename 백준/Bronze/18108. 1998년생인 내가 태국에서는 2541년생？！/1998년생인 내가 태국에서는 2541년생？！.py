import sys

def main() -> None:
    data = sys.stdin.readline().strip()
    if not data:
        return
    year = int(data)
    print(year - 543)

if __name__ == '__main__':
    main()
