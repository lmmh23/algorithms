import sys

def main() -> None:
    data = sys.stdin.readline().strip().split()
    if len(data) != 2:
        return
    n, k = map(int, data)
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    if k > len(divisors):
        print(0)
    else:
        print(divisors[k - 1])

if __name__ == '__main__':
    main()
