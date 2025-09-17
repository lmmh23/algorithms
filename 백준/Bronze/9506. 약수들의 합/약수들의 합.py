import sys

def proper_divisors(n: int) -> list[int]:
    divisors = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    if n == 1:
        return []
    return sorted(divisors)

def main() -> None:
    outputs = []
    for line in sys.stdin:
        value = int(line)
        if value == -1:
            break
        divisors = proper_divisors(value)
        if sum(divisors) == value:
            decomposition = ' + '.join(map(str, divisors))
            outputs.append(f"{value} = {decomposition}")
        else:
            outputs.append(f"{value} is NOT perfect.")
    sys.stdout.write('
'.join(outputs))

if __name__ == '__main__':
    main()
