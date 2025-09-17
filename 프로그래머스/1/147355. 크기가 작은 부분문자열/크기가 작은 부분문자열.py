def solution(t: str, p: str) -> int:
    target = int(p)
    length = len(p)
    count = 0
    for idx in range(len(t) - length + 1):
        if int(t[idx:idx + length]) <= target:
            count += 1
    return count
