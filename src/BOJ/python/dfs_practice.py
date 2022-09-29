# # 5-8.py
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]


# visited = [False] * 9
# dfs(graph, 1, visited)

# 음료수 얼려먹기

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if graph[x][y] > 0:
        graph[x][y] = 0
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)

        return True
    return False

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)