def solution(n, words):
    seen = set()

    for i in range(len(words)):
        is_first_index = i == 0
        prev_word = words[i - 1] if not is_first_index else ""
        cur_word = words[i]

        is_exist = cur_word in seen
        if not is_exist:
            seen.add(cur_word)

        failed = False if is_first_index else prev_word[-1] != cur_word[0]

        if is_exist or failed:
            person = n if (i + 1) % n == 0 else (i % n) + 1
            turn = i // n + 1
            return [person, turn]

    return [0, 0]
