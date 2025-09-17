def solution(s: str) -> str:
    result = []
    idx = 0
    for ch in s:
        if ch == ' ':
            result.append(ch)
            idx = 0
        else:
            if idx % 2 == 0:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
            idx += 1
    return ''.join(result)
