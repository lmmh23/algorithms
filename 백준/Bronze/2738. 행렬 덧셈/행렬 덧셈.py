import sys

def main() -> None:
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(map(int, input_data))
    n = next(it)
    m = next(it)
    first = [[next(it) for _ in range(m)] for _ in range(n)]
    second = [[next(it) for _ in range(m)] for _ in range(n)]
    result_lines = []
    for i in range(n):
        summed = [str(first[i][j] + second[i][j]) for j in range(m)]
        result_lines.append(' '.join(summed))
    sys.stdout.write('
'.join(result_lines))

if __name__ == '__main__':
    main()
