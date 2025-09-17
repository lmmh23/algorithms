from typing import List

def _rank(matches: int) -> int:
    mapping = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    return mapping.get(matches, 6)

def solution(lottos: List[int], win_nums: List[int]) -> List[int]:
    zero_count = lottos.count(0)
    matched = len(set(lottos) & set(win_nums))
    best = _rank(matched + zero_count)
    worst = _rank(matched)
    return [best, worst]
