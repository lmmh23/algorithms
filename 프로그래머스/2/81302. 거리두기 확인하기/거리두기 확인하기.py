from collections import deque
from typing import List

def is_safe(place: List[str]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r in range(5):
        for c in range(5):
            if place[r][c] != 'P':
                continue
            visited = [[False] * 5 for _ in range(5)]
            visited[r][c] = True
            queue = deque([(r, c, 0)])
            while queue:
                x, y, dist = queue.popleft()
                if dist >= 2:
                    continue
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < 5 and 0 <= ny < 5):
                        continue
                    if visited[nx][ny] or place[nx][ny] == 'X':
                        continue
                    if place[nx][ny] == 'P':
                        return 0
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    return 1

def solution(places: List[List[str]]) -> List[int]:
    return [is_safe(place) for place in places]
