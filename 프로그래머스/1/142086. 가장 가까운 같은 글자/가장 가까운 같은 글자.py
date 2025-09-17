from typing import List

def solution(s: str) -> List[int]:
    last_seen = {}
    result = []
    for index, char in enumerate(s):
        if char not in last_seen:
            result.append(-1)
        else:
            result.append(index - last_seen[char])
        last_seen[char] = index
    return result
