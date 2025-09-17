def solution(n: int, w: int, num: int) -> int:
    row = (num - 1) // w
    if row % 2 == 0:
        col = (num - 1) % w
    else:
        col = w - 1 - (num - 1) % w
    answer = 0
    max_row = (n - 1) // w
    for current_row in range(row, max_row + 1):
        if current_row % 2 == 0:
            box_num = current_row * w + (col + 1)
        else:
            box_num = current_row * w + (w - col)
        if box_num > n:
            break
        answer += 1
    return answer
