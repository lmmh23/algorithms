import sys
from collections import Counter
s=sys.stdin.readline().strip().upper()
count=Counter(s)
max_cnt=max(count.values())
chars=[ch for ch,cnt in count.items() if cnt==max_cnt]
print(chars[0] if len(chars)==1 else '?')
