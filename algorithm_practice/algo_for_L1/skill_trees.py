def solution(skill, skill_trees):
    answer = 0
    for i, skill_tree in enumerate(skill_trees):
        idx = 0
        for j in skill_tree:
            if j in skill:
                if skill[idx] == j:
                    idx += 1
                else:
                    break
        else:
            answer += 1

    return answer