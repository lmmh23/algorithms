import sys

def main() -> None:
    data = sys.stdin.readline().strip()
    if not data:
        return
    n = int(data)
    lines = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    sys.stdout.write('
'.join(lines))

if __name__ == '__main__':
    main()
