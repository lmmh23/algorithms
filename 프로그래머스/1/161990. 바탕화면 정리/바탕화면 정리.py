from typing import List

def solution(wallpaper: List[str]) -> List[int]:
    rows = [i for i, row in enumerate(wallpaper) if '#' in row]
    cols = [j for j in range(len(wallpaper[0])) if any(row[j] == '#' for row in wallpaper)]
    top = min(rows)
    left = min(cols)
    bottom = max(rows) + 1
    right = max(cols) + 1
    return [top, left, bottom, right]
