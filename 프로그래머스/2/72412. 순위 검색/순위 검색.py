from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    table = defaultdict(list)
    
    for line in info:
        lang, job, position, food, score = line.split()
        score = int(score)
        attrs = [lang, job, position, food]
        
        # 총 경우의 수는 2*2*2*2=24
        for mask in range(16):
            keyArr = []
            # attrs의 개수만큼 반복 len(attrs)=4
            for i in range(4):
                # ..?
                if mask & (1 << i):
                    keyArr.append('-')
                else:
                    keyArr.append(attrs[i])
            key = ' '.join(keyArr)
            table[key].append(score)
            
    for key in table:
        table[key].sort()
            
            
    answer = []
        
    for q in query:
        q = q.replace(" and ", " ")
            
        *conds, score = q.split()
        score = int(score)
        key = ' '.join(conds)
            
        if key not in table:
            answer.append(0)
            continue
            
        scores = table[key]
        idx = bisect_left(scores, score)
        answer.append(len(scores) - idx)
    
    return answer