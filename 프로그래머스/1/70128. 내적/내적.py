from typing import List

def solution(a: List[int], b: List[int]) -> int:
    return sum(x * y for x, y in zip(a, b))
