def solution(a: int, b: int, n: int) -> int:
    total = 0
    current = n
    while current >= a:
        exchanged = (current // a) * b
        total += exchanged
        current = exchanged + current % a
    return total
