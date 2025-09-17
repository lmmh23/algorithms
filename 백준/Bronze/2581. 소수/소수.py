import sys

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    m, n = map(int, data)
    primes = [num for num in range(m, n + 1) if is_prime(num)]
    if not primes:
        print(-1)
        return
    print(sum(primes))
    print(primes[0])

if __name__ == '__main__':
    main()
