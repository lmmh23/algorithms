from typing import List

def solution(ingredient: List[int]) -> int:
    stack: List[int] = []
    count = 0
    for item in ingredient:
        stack.append(item)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            count += 1
    return count
