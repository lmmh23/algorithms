from typing import Dict, List

PARENT: Dict[str, str] = {}
PROFIT: Dict[str, int] = {}

UNIT_PRICE = 100


def distribute(name: str, money: int) -> None:
    if name == 'none' or money == 0:
        return
    commission = money // 10
    PROFIT[name] = PROFIT.get(name, 0) + money - commission
    if commission == 0:
        return
    distribute(PARENT.get(name, 'none'), commission)


def normalize_parent(value: str) -> str:
    if value.strip() == '-':
        return 'none'
    return value


def solution(enroll: List[str], referral: List[str], seller: List[str], amount: List[int]) -> List[int]:
    PARENT.clear()
    PROFIT.clear()
    for person, parent in zip(enroll, referral):
        PARENT[person] = normalize_parent(parent)
        PROFIT[person] = 0
    for person, cnt in zip(seller, amount):
        distribute(person, cnt * UNIT_PRICE)
    return [PROFIT[name] for name in enroll]
