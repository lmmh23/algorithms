from typing import List

def solution(k: int, m: int, score: List[int]) -> int:
    score.sort(reverse=True)
    total = 0
    for idx in range(m - 1, len(score), m):
        total += score[idx] * m
    return total
