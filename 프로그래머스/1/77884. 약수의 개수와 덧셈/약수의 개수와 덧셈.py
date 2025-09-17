def divisor_count(num: int) -> int:
    count = 0
    root = int(num ** 0.5)
    for i in range(1, root + 1):
        if num % i == 0:
            count += 1 if i == num // i else 2
    return count

def solution(left: int, right: int) -> int:
    total = 0
    for value in range(left, right + 1):
        if divisor_count(value) % 2 == 0:
            total += value
        else:
            total -= value
    return total
