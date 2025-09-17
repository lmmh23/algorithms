import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    values = list(map(int, data))
    max_value = max(values)
    idx = values.index(max_value)
    row = idx // 9 + 1
    col = idx % 9 + 1
    print(max_value)
    print(row, col)

if __name__ == '__main__':
    main()
