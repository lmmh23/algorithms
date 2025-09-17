import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    t = next(it)
    coins = [25, 10, 5, 1]
    outputs = []
    for _ in range(t):
        c = next(it)
        counts = []
        for coin in coins:
            count, c = divmod(c, coin)
            counts.append(str(count))
        outputs.append(' '.join(counts))
    sys.stdout.write('
'.join(outputs))

if __name__ == '__main__':
    main()
