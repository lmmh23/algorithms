answer = 0

def BFS(numbers, target, total, index):
    global answer
    if index == len(numbers):
        if total == target:
            answer += 1
        return

    BFS(numbers, target, total + numbers[index], index + 1)
    BFS(numbers, target, total - numbers[index], index + 1)


def solution(numbers, target):
    global answer
    answer = 0  # 매번 초기화해야 여러 번 호출 시 누적되지 않음
    BFS(numbers, target, 0, 0)
    return answer
