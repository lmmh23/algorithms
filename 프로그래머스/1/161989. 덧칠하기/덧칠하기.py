from typing import List

def solution(n: int, m: int, section: List[int]) -> int:
    painted = 0
    count = 0
    for start in section:
        if start > painted:
            painted = start + m - 1
            count += 1
    return count
