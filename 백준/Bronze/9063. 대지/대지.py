import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    n = next(it)
    xs = []
    ys = []
    for _ in range(n):
        xs.append(next(it))
        ys.append(next(it))
    if n < 2:
        print(0)
        return
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    print(width * height)

if __name__ == '__main__':
    main()
