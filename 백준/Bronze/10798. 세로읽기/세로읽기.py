import sys

lines = [sys.stdin.readline().strip() for _ in range(5)]
max_len = max(len(line) for line in lines)
result = []
for c in range(max_len):
    for r in range(5):
        if c < len(lines[r]):
            result.append(lines[r][c])
print(''.join(result))

