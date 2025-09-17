from typing import List

def solution(nums: List[int]) -> int:
    return min(len(set(nums)), len(nums) // 2)
