import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    total = next(it)
    n = next(it)
    calculated = 0
    for _ in range(n):
        price = next(it)
        quantity = next(it)
        calculated += price * quantity
    print('Yes' if calculated == total else 'No')

if __name__ == '__main__':
    main()
