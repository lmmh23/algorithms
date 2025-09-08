def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        order = [c for c in tree if c in skill]
        if order == list(skill[:len(order)]):
            answer += 1
    return answer

