import sys

def main() -> None:
    data = sys.stdin.readline().strip()
    if not data:
        return
    n = int(data)
    dots = 2
    for _ in range(n):
        dots = dots * 2 - 1
    print(dots * dots)

if __name__ == '__main__':
    main()
