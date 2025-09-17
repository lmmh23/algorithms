from typing import List

def solution(keymap: List[str], targets: List[str]) -> List[int]:
    key_cost = {}
    for key in keymap:
        for idx, char in enumerate(key):
            key_cost[char] = min(key_cost.get(char, idx + 1), idx + 1)
    result = []
    for target in targets:
        total = 0
        for char in target:
            if char not in key_cost:
                total = -1
                break
            total += key_cost[char]
        result.append(total)
    return result
