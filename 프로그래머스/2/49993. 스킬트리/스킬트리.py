def solution(skill, skill_trees):
    answer = 0
    skill = list(map(str, skill.strip()))
    for skill_tree in skill_trees:
        if isValid(skill, skill_tree): answer += 1
    return answer

def isValid(skill, skill_tree) -> bool:
    skill_tree = [item for item in skill_tree if item in skill]
    n = len(skill_tree)
    return skill[:n] == skill_tree