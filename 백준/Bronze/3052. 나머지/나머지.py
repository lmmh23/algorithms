rest = []

for i in range(10):
  n = int(input())
  rest.append(n % 42)

print(len(list(set(rest))))