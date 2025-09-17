import sys

def main() -> None:
    data = sys.stdin.readline().strip()
    if not data:
        return
    n = int(data)
    print(4 * n)

if __name__ == '__main__':
    main()
