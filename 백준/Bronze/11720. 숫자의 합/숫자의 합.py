import sys

def main() -> None:
    sys.stdin.readline()  # discard length
    digits = sys.stdin.readline().strip()
    if not digits:
        print(0)
        return
    print(sum(int(ch) for ch in digits))

if __name__ == '__main__':
    main()
