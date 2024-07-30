def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        if isValid(skill, skill_tree): answer += 1
    return answer

def isValid(skill, skill_tree) -> bool:
    """
    skill := "CBD"
    skill_tree := "BACDE", "CBADF", ...
    
    """
    res = ''.join([item for item in skill_tree if item in skill])
    n = len(res)
    return skill[:n] == res