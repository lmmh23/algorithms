from typing import List

def solution(numbers: List[int]) -> int:
    missing = [digit for digit in range(10) if digit not in numbers]
    if not missing:
        return -1
    return sum(missing)
