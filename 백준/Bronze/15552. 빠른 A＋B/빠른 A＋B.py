import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    t = next(it)
    outputs = []
    for _ in range(t):
        a = next(it)
        b = next(it)
        outputs.append(str(a + b))
    sys.stdout.write('
'.join(outputs))

if __name__ == '__main__':
    main()
