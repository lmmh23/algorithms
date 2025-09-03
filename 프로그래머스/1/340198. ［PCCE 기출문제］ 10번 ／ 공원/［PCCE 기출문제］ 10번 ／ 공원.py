def solution(mats, park):
    R, C = len(park), len(park[0])
    answer = -1
    
    blank = []
    for i in range(R):
        for j in range(C):
            if park[i][j] == "-1":
                blank.append((i, j))
                
    for x, y in blank:
        for mat in mats:
            if x + mat > R or y + mat > C:
                continue

            possible = True
            for i in range(mat):
                for j in range(mat):
                    if park[x + i][y + j] != "-1":
                        possible = False
                        break
                if not possible:
                    break

            if possible:
                answer = max(answer, mat)
    
    return answer