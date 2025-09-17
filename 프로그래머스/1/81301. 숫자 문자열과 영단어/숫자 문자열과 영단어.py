def solution(s: str) -> int:
    mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    result = ''
    buffer = ''
    for ch in s:
        if ch.isdigit():
            result += ch
            buffer = ''
            continue
        buffer += ch
        if buffer in mapping:
            result += mapping[buffer]
            buffer = ''
    return int(result)
