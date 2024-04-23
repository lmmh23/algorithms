arr = []

for _ in range(28):
  num = int(input())
  arr.append(num)

missingNums = []

for i in range(1, 31):
  if i not in arr:
    missingNums.append(i)
    
print(min(missingNums))
print(max(missingNums))
