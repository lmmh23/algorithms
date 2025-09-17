import heapq
from math import inf
from typing import List

def solution(board: List[List[int]]) -> int:
    n = len(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    costs = [[[inf] * 4 for _ in range(n)] for _ in range(n)]
    pq: list[tuple[int, int, int, int]] = [(0, 0, 0, -1)]
    for d in range(4):
        costs[0][0][d] = 0

    while pq:
        cost, row, col, prev_dir = heapq.heappop(pq)
        if (row, col) == (n - 1, n - 1):
            return cost
        for idx, (dr, dc) in enumerate(directions):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if board[nr][nc] == 1:
                continue
            next_cost = cost + 100
            if prev_dir != -1 and prev_dir != idx:
                if ((prev_dir < 2 and idx >= 2) or (prev_dir >= 2 and idx < 2)):
                    next_cost += 500
            if next_cost < costs[nr][nc][idx]:
                costs[nr][nc][idx] = next_cost
                heapq.heappush(pq, (next_cost, nr, nc, idx))
    return min(costs[n - 1][n - 1])
