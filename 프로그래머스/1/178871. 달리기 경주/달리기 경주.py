from typing import Dict, List

def solution(players: List[str], callings: List[str]) -> List[str]:
    positions: Dict[str, int] = {player: idx for idx, player in enumerate(players)}
    for name in callings:
        idx = positions[name]
        if idx == 0:
            continue
        ahead = players[idx - 1]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        positions[name] -= 1
        positions[ahead] += 1
    return players
