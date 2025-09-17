import sys

def main() -> None:
    outputs = []
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        if b % a == 0:
            outputs.append('factor')
        elif a % b == 0:
            outputs.append('multiple')
        else:
            outputs.append('neither')
    sys.stdout.write('
'.join(outputs))

if __name__ == '__main__':
    main()
