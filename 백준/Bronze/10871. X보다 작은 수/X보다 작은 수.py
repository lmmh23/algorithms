N, X = map(int, input().split())
numbers = list(map(int, input().split()))

for item in numbers:
  if (item < X):
    print(item, end = " ")