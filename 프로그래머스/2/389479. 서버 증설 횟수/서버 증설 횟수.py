from typing import List

def solution(players: List[int], m: int, k: int) -> int:
    activated = [0] * len(players)
    running = 0
    added_total = 0
    for idx, count in enumerate(players):
        if idx >= k:
            running -= activated[idx - k]
        required = count // m
        if required > running:
            add = required - running
            running += add
            added_total += add
            activated[idx] = add
    return added_total
