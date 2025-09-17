from typing import List

def solution(answers: List[int]) -> List[int]:
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    scores = [0, 0, 0]
    for idx, answer in enumerate(answers):
        if patterns[0][idx % len(patterns[0])] == answer:
            scores[0] += 1
        if patterns[1][idx % len(patterns[1])] == answer:
            scores[1] += 1
        if patterns[2][idx % len(patterns[2])] == answer:
            scores[2] += 1
    max_score = max(scores, default=0)
    return [idx + 1 for idx, score in enumerate(scores) if score == max_score]
