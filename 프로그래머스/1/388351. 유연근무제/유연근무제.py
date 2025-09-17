from typing import List

MAX_WEEKDAYS = 7

def add_minutes(time: int, minutes: int) -> int:
    hour, minute = divmod(time, 100)
    minute += minutes
    hour += minute // 60
    minute %= 60
    return hour * 100 + minute

def solution(schedules: List[int], timelogs: List[List[int]], startday: int) -> int:
    answer = 0
    for schedule, logs in zip(schedules, timelogs):
        latest = add_minutes(schedule, 10)
        day = startday
        success = True
        for log in logs:
            if day > 5:
                day = day % MAX_WEEKDAYS + 1
                continue
            if log > latest:
                success = False
            day = (day + 1) % MAX_WEEKDAYS
        if success:
            answer += 1
    return answer
