numbers = []

for i in range(9):
  num = int(input())
  numbers.append(num)

maxVal = max(numbers)

print(maxVal)
print(numbers.index(maxVal) + 1)