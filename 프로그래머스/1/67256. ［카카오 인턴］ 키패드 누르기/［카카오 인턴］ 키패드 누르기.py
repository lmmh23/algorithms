def solution(numbers, hand):
    answer = ''
    
    # 키보드 좌표 설정
    pos = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2),
        '*': (0, 3), 0: (1, 3), '#': (2, 3)
    }
    
    leftPos = pos['*']
    rightPos = pos['#']
    
    
    for num in numbers:
        if num in [1,4,7]:
            # 1,4,7이면 왼쪽
            answer += 'L'
            leftPos = pos[num]
        elif num in [3,6,9]:
            # 3,6,9이면 오른쪽
            answer += 'R'
            rightPos = pos[num]
        else:
            # 나머지에 대해서 거리 계산
            dL = dist(leftPos, pos[num])
            dR = dist(rightPos, pos[num])

            if dL < dR:
                answer += 'L'
                leftPos = pos[num]
            elif dL > dR:
                answer += 'R'
                rightPos = pos[num]
            else:
                if hand == 'right':
                    answer += 'R'
                    rightPos = pos[num]
                elif hand == 'left':
                    answer += 'L'
                    leftPos = pos[num]
    return answer

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])