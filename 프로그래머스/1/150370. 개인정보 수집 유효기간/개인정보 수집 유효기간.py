from typing import Dict, List

DAYS_PER_MONTH = 28
MONTHS_PER_YEAR = 12

def to_days(date: str) -> int:
    year, month, day = map(int, date.split('.'))
    return (year * MONTHS_PER_YEAR + month) * DAYS_PER_MONTH + day

def solution(today: str, terms: List[str], privacies: List[str]) -> List[int]:
    expiration: Dict[str, int] = {}
    for term in terms:
        key, months = term.split()
        expiration[key] = int(months)
    today_days = to_days(today)
    expired_indices = []
    for idx, privacy in enumerate(privacies, start=1):
        date_str, term_key = privacy.split()
        start_days = to_days(date_str)
        expiry_days = start_days + expiration[term_key] * DAYS_PER_MONTH - 1
        if today_days > expiry_days:
            expired_indices.append(idx)
    return expired_indices
