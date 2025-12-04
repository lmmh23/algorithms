def solution(dartResult):
    dartResult = dartResult.replace("10", "k")
    
    stack = []
    
    for char in dartResult:
        if char.isdigit():
            stack.append(int(char))
        elif char == 'k':
            stack.append(10)
        elif char == 'S':
            pass
        elif char == 'D':
            stack[-1] **= 2
        elif char == 'T':
            stack[-1] **= 3
        elif char == '*':
            if len(stack) > 1:
                stack[-2] *= 2
            stack[-1] *= 2
        elif char == '#':
            stack[-1] *= -1
    
    return sum(stack)