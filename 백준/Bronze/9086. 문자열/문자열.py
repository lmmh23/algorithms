import sys

def main() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return
    t = int(data[0])
    outputs = []
    for line in data[1:1 + t]:
        outputs.append(line[0] + line[-1])
    sys.stdout.write('
'.join(outputs))

if __name__ == '__main__':
    main()
