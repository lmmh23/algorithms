import math

def is_prime(n):
    if n < 2:  # 1 이하는 소수 아님
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 세기
cnt = 0
for k in numbers:
    if is_prime(k):
        cnt += 1

print(cnt)
