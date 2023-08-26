from itertools import permutations
N, R = 0, 0
answer = set()
def check_id(id, condition):
    if len(condition) != len(id): return False

    for i in range(len(id)):
        if condition[i] == '*': continue
        if condition[i] != id[i]: return False
    return True

def isValid(p, banned_id):
    global answer
    
    for i in range(len(p)):
        if not check_id(p[i], banned_id[i]): return False
    
    p = set(p)
    answer.add(frozenset(p))
    return True


def solution(user_id, banned_id):
    R = len(banned_id)
    perm = list(permutations(user_id, R))
    
    for p in perm:
        isValid(p, banned_id)
        
    print(answer)
    return len(answer)