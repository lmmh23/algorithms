import sys

def main() -> None:
    data = sys.stdin.readline().strip()
    if not data:
        return
    n = int(data)
    repeat = n // 4
    print('long ' * repeat + 'int')

if __name__ == '__main__':
    main()
