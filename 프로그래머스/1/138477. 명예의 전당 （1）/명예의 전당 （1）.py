import heapq
from typing import List

def solution(k: int, score: List[int]) -> List[int]:
    hall: List[int] = []
    result: List[int] = []
    for value in score:
        heapq.heappush(hall, value)
        if len(hall) > k:
            heapq.heappop(hall)
        result.append(hall[0])
    return result
