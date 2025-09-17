import sys

def classify(a: int, b: int, c: int) -> str:
    sides = sorted((a, b, c))
    if sides[2] >= sides[0] + sides[1]:
        return 'Invalid'
    if sides[0] == sides[1] == sides[2]:
        return 'Equilateral'
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return 'Isosceles'
    return 'Scalene'

def main() -> None:
    results = []
    for line in sys.stdin:
        a, b, c = map(int, line.split())
        if a == b == c == 0:
            break
        results.append(classify(a, b, c))
    sys.stdout.write('
'.join(results))

if __name__ == '__main__':
    main()
