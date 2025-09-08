def solution(number, k):
    answer = ""
    n = len(number) - k
    idx = -1

    for i in range(n):
        max_digit = '0'
        for j in range(idx + 1, k + i + 1):
            if max_digit < number[j]:
                max_digit = number[j]
                idx = j
        answer += max_digit

    return answer