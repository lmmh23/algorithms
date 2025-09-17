import sys

def main() -> None:
    data = sys.stdin.readline().strip()
    if not data:
        return
    n = int(data)
    factor = 2
    outputs = []
    while factor * factor <= n:
        while n % factor == 0:
            outputs.append(str(factor))
            n //= factor
        factor += 1
    if n > 1:
        outputs.append(str(n))
    if outputs:
        sys.stdout.write('
'.join(outputs))

if __name__ == '__main__':
    main()
