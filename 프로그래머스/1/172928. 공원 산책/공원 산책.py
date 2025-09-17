from typing import List

def solution(park: List[str], routes: List[str]) -> List[int]:
    rows = len(park)
    cols = len(park[0]) if rows else 0
    start = [0, 0]
    for r, line in enumerate(park):
        c = line.find('S')
        if c != -1:
            start = [r, c]
            break
    current = start[:]
    direction_map = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1),
    }
    for route in routes:
        direction, dist_str = route.split()
        dr, dc = direction_map[direction]
        distance = int(dist_str)
        nr, nc = current
        blocked = False
        for _ in range(distance):
            nr += dr
            nc += dc
            if not (0 <= nr < rows and 0 <= nc < cols) or park[nr][nc] == 'X':
                blocked = True
                break
        if not blocked:
            current = [nr, nc]
    return current
