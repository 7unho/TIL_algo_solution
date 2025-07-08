"""
answer := 도달할 수 있다면 a의 최솟값 없다면 -1
n = a의 최소 개수
m = b의 최소 개수
"""
answer = -1
visited = set()
STEP = 0
A = 0
B = 1
def process(depth, sum_a, sum_b, info):
    global answer, STEP
    if sum_a <= 0 or sum_b <= 0:
        return
    
    if depth == STEP:
        answer = max(answer, sum_a)
        return
    
    if (depth + 1, sum_a - info[depth][A], sum_b) not in visited:
        visited.add((depth + 1, sum_a - info[depth][A], sum_b))
        process(depth + 1, sum_a - info[depth][A], sum_b, info)
        
    if (depth + 1, sum_a, sum_b - info[depth][B]) not in visited:
        visited.add((depth + 1, sum_a, sum_b - info[depth][B]))
        process(depth + 1, sum_a, sum_b - info[depth][B], info)

def solution(info, n, m):
    global answer, STEP
    STEP = len(info)
    process(0, n, m, info)
    return answer if answer == -1 else n - answer