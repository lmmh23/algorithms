from typing import List

def solution(s: str, n: int) -> str:
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            offset = (ord(ch) - ord('a') + n) % 26
            result.append(chr(ord('a') + offset))
        elif 'A' <= ch <= 'Z':
            offset = (ord(ch) - ord('A') + n) % 26
            result.append(chr(ord('A') + offset))
        else:
            result.append(ch)
    return ''.join(result)
