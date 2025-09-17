def solution(price: int, money: int, count: int) -> int:
    total = price * count * (count + 1) // 2
    return max(total - money, 0)
