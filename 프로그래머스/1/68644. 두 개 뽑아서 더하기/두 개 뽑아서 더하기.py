from itertools import combinations
from typing import List

def solution(numbers: List[int]) -> List[int]:
    sums = {a + b for a, b in combinations(numbers, 2)}
    return sorted(sums)
