from typing import List

def solution(bandage: List[int], health: int, attacks: List[List[int]]) -> int:
    cast_time, heal_per_second, bonus_heal = bandage
    current = health
    for idx, (time, damage) in enumerate(attacks):
        current -= damage
        if current <= 0:
            return -1
        if idx == len(attacks) - 1:
            break
        next_time = attacks[idx + 1][0]
        gap = next_time - time - 1
        if gap <= 0:
            continue
        full_casts, _ = divmod(gap, cast_time)
        current += gap * heal_per_second + full_casts * bonus_heal
        if current > health:
            current = health
    return -1 if current <= 0 else current
