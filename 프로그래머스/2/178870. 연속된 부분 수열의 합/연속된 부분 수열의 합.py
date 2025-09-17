from typing import List

def solution(sequence: List[int], k: int) -> List[int]:
    left = 0
    current = 0
    best: List[int] | None = None
    for right, value in enumerate(sequence):
        current += value
        while current > k and left <= right:
            current -= sequence[left]
            left += 1
        while current == k and left <= right:
            candidate = [left, right]
            if best is None:
                best = candidate
            else:
                best_len = best[1] - best[0]
                cand_len = candidate[1] - candidate[0]
                if cand_len < best_len or (cand_len == best_len and candidate[0] < best[0]):
                    best = candidate
            current -= sequence[left]
            left += 1
    return best if best is not None else [0, 0]
