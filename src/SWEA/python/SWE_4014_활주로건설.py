# N * N 의 활주로 건설
def check(row):
    global N, X
    cnt = 1
    for i in range(1, N):
        if row[i] == row[i-1]:	# 같은 높이라면
            cnt += 1
        elif row[i] - row[i-1] == 1 and cnt >= X:   # 높이 1 높아지면
            cnt = 1
        elif row[i-1] - row[i] == 1 and cnt >= 0:   # 높이 1 낮아지면
            cnt = -X + 1
        else:   # 높이 2 이상 차이나면
            return 0
    if cnt >= 0:
        return 1
    return 0

for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        answer += check(graph[i])
        
        temp = []
        for j in range(N):
            temp.append(graph[j][i])
        
        answer += check(temp)

    print(f"#{tc} {answer}")
