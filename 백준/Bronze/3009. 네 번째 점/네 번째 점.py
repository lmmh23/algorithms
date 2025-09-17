import sys

def main() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) != 6:
        return
    xs = [data[i] for i in range(0, 6, 2)]
    ys = [data[i] for i in range(1, 6, 2)]
    def unique(coord):
        if coord[0] == coord[1]:
            return coord[2]
        if coord[0] == coord[2]:
            return coord[1]
        return coord[0]
    print(unique(xs), unique(ys))

if __name__ == '__main__':
    main()
