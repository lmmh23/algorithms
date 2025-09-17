def solution(s: str) -> int:
    answer = 0
    first = None
    same = 0
    diff = 0
    for ch in s:
        if first is None:
            first = ch
            same = 1
            diff = 0
            continue
        if ch == first:
            same += 1
        else:
            diff += 1
        if same == diff:
            answer += 1
            first = None
            same = 0
            diff = 0
    if first is not None:
        answer += 1
    return answer
