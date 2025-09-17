import sys
import math

def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        return
    a, b, v = map(int, data)
    if a >= v:
        print(1)
        return
    remaining = v - a
    daily_gain = a - b
    days = 1 + math.ceil(remaining / daily_gain)
    print(days)

if __name__ == '__main__':
    main()
