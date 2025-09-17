import sys

def main() -> None:
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    t = int(data[0])
    results = []
    for line in data[1:1 + t]:
        repeat, text = line.split()
        r = int(repeat)
        expanded = ''.join(ch * r for ch in text)
        results.append(expanded)
    sys.stdout.write('
'.join(results))

if __name__ == '__main__':
    main()
