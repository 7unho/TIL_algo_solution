def make_queen(graph, cnt):
    global answer, n
    
    if cnt == n:
        answer += 1
        return

    temp = [0] * n

    for i in range(len(graph)):
        temp[graph[i]] = 1

        if graph[i] - (cnt - i) >= 0:
            temp[graph[i] - (cnt - i)] = 1
        
        if graph[i] + (cnt - i) < n:
            temp[graph[i] + (cnt - i)] = 1

    for j in range(n):
        if temp[j] == 0:
            make_queen(graph + [j], cnt + 1)
        
for i in range(int(input())):
    n = int(input())
    answer = 0
    make_queen([], 0)

    print(f"#{i + 1} {answer}")