from collections import deque
from typing import List

def solution(cards1: List[str], cards2: List[str], goal: List[str]) -> str:
    deck1 = deque(cards1)
    deck2 = deque(cards2)
    for word in goal:
        if deck1 and deck1[0] == word:
            deck1.popleft()
        elif deck2 and deck2[0] == word:
            deck2.popleft()
        else:
            return 'No'
    return 'Yes'
