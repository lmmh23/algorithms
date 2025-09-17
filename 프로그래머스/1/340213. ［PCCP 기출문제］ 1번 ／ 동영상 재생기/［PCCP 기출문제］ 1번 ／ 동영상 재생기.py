from typing import List

def to_second(value: str) -> int:
    minute, second = map(int, value.split(':'))
    return minute * 60 + second

def to_time(second: int) -> str:
    minute, sec = divmod(second, 60)
    return f"{minute:02d}:{sec:02d}"

def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: List[str]) -> str:
    video_length = to_second(video_len)
    current = to_second(pos)
    op_start_sec = to_second(op_start)
    op_end_sec = to_second(op_end)

    if op_start_sec <= current <= op_end_sec:
        current = op_end_sec

    for command in commands:
        if command == 'next':
            current += 10
        else:
            current -= 10
        current = min(max(current, 0), video_length)
        if op_start_sec <= current <= op_end_sec:
            current = op_end_sec
    return to_time(current)
