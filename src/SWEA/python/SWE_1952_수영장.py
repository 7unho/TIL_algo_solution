def dfs(depth, sum):
    global answer
    # 종료 조건 ( 기저 조건 )
    if sum > answer:
        return

    if depth > 12:
        answer = min(sum, answer)
        return

    if graph[depth] == 0:
        dfs(depth + 1, sum)
        return
    
    dfs(depth + 1, sum + graph[depth] * day)
    dfs(depth + 1, sum + month)
    dfs(depth + 3, sum + month_3)
    

for tc in range(1, int(input()) + 1):
    graph = [0]
    day, month, month_3, year = map(int, input().split())
    graph += list(map(int, input().split()))

    answer = year
    dfs(1, 0)

    print(f"#{tc} {answer}")

