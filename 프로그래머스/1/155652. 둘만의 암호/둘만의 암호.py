def solution(s: str, skip: str, index: int) -> str:
    skip_set = set(skip)
    result_chars = []
    for ch in s:
        steps = 0
        current = ord(ch)
        while steps < index:
            current = (current - 97 + 1) % 26 + 97
            if chr(current) in skip_set:
                continue
            steps += 1
        result_chars.append(chr(current))
    return ''.join(result_chars)
