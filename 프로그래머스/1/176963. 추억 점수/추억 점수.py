from typing import Dict, List

def solution(name: List[str], yearning: List[int], photo: List[List[str]]) -> List[int]:
    scores: Dict[str, int] = dict(zip(name, yearning))
    result = []
    for group in photo:
        total = sum(scores.get(person, 0) for person in group)
        result.append(total)
    return result
