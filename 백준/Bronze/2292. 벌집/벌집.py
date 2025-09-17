import sys

def main() -> None:
    data = sys.stdin.readline().strip()
    if not data:
        return
    n = int(data)
    layer = 1
    max_num = 1
    while n > max_num:
        max_num += 6 * layer
        layer += 1
    print(layer)

if __name__ == '__main__':
    main()
