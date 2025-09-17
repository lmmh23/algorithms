import sys

def main() -> None:
    a, b = sys.stdin.readline().strip().split()
    ra = int(a[::-1])
    rb = int(b[::-1])
    print(max(ra, rb))

if __name__ == '__main__':
    main()
