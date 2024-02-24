T = int(input())

for case in range(1, T+1):
  x, y = map(int, input().split())
  result = x + y
  
  print("Case #{}: {}".format(case, result))