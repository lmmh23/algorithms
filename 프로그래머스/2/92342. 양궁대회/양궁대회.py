from typing import List

max_diff = -1
best: List[int] = []

def dfs(idx: int, arrows: int, apeach: List[int], ryan: List[int]) -> None:
    global max_diff, best
    if idx == 11 or arrows == 0:
        if arrows > 0:
            ryan[10] += arrows
        apeach_score = ryan_score = 0
        for score in range(11):
            if apeach[score] == 0 and ryan[score] == 0:
                continue
            if ryan[score] > apeach[score]:
                ryan_score += 10 - score
            else:
                apeach_score += 10 - score
        diff = ryan_score - apeach_score
        if diff > 0:
            if diff > max_diff:
                max_diff = diff
                best = ryan[:]
            elif diff == max_diff:
                for idx_reverse in range(10, -1, -1):
                    if ryan[idx_reverse] > best[idx_reverse]:
                        best = ryan[:]
                        break
                    if ryan[idx_reverse] < best[idx_reverse]:
                        break
        if arrows > 0:
            ryan[10] -= arrows
        return

    needed = apeach[idx] + 1
    if needed <= arrows:
        ryan[idx] = needed
        dfs(idx + 1, arrows - needed, apeach, ryan)
        ryan[idx] = 0
    dfs(idx + 1, arrows, apeach, ryan)


def solution(n: int, info: List[int]) -> List[int]:
    global max_diff, best
    max_diff = -1
    best = [-1]
    dfs(0, n, info, [0] * 11)
    return best if max_diff > 0 else [-1]
