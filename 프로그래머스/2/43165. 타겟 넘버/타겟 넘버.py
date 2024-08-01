answer = 0
n = 0
def solution(numbers, target):
    global n
    n = len(numbers)
    dfs(0, 0, numbers, target)
    return answer

def dfs(depth, sum, numbers, target):
    global answer
    if depth == n:
        if sum == target:
            answer += 1
        return
    
    dfs(depth + 1, sum + numbers[depth], numbers, target)
    dfs(depth + 1, sum - numbers[depth], numbers, target)