N, M = map(int, input().split())
numbers = [0] * N

for _ in range(M):
  i, j, k = map(int, input().split())
  for index in range(i, j+1):
    numbers[index - 1] = k

print(*numbers)

