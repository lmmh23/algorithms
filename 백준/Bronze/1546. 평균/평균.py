# 입력 받기
N = int(input())
scores = list(map(int, input().split()))
    
# 최댓값 찾기
max_score = max(scores)
    
# 새로운 점수 계산 및 평균 구하기
new_scores = [(score / max_score) * 100 for score in scores]
average = sum(new_scores) / N
    
# 결과 출력 (소수 둘째 자리까지)
print(f"{average:.2f}")