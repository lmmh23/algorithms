def solution(dirs: str) -> int:
    x = y = 0
    visited = set()
    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    for command in dirs:
        dx, dy = moves[command]
        nx, ny = x + dx, y + dy
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        edge = ((x, y), (nx, ny))
        reverse = ((nx, ny), (x, y))
        if edge not in visited:
            visited.add(edge)
            visited.add(reverse)
        x, y = nx, ny
    return len(visited) // 2
