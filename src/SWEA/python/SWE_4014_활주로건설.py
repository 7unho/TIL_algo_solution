def check(temp):
    global N, X
    cnt = 1

    for i in range(1, N):
        if temp[i] == temp[i - 1] : cnt += 1
        elif temp[i] - 1 == temp[i - 1] and cnt >= X: cnt = 1
        elif temp[i] + 1 == temp[i - 1] and cnt >= 0: cnt = -X + 1
        else: return 0
    
    if cnt >= 0: return 1
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
