from typing import List

def solution(array: List[int], commands: List[List[int]]) -> List[int]:
    result = []
    for i, j, k in commands:
        sliced = array[i - 1:j]
        sliced.sort()
        result.append(sliced[k - 1])
    return result
