def cal(a, b, idx):
    if idx == 0:
        return a + b
    elif idx == 1:
        return a - b
    elif idx == 2:
        return a * b
    else:
        return int(a / b)

def dfs(depth, res):
    global MAX, MIN
    if depth == N - 1:
        MAX = max(MAX, res)
        MIN = min(MIN, res)
        return
    
    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            dfs(depth + 1, cal(res, numbers[depth + 1], i))
            oper[i] += 1

for tc in range(1, int(input()) + 1):
    N = int(input())
    oper = list(map(int, input().split()))
    MAX = -100_000_001
    MIN = 100_000_001
    numbers = list(map(int, input().split()))

    dfs(0, numbers[0])
    print(f"#{tc} {MAX - MIN}")