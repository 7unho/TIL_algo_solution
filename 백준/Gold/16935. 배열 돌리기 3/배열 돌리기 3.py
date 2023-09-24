import sys
from copy import deepcopy
input = sys.stdin.readline

# 입력값 : N(행), M(열), R(연산 횟수)
# 출력값 : 입력으로 주어진 배열에 R번의 연산을 순서대로 수행한 결과

def printGraph(graph):
    for i in range(len(graph)):
        print(graph[i])
    print()

def makeSubGraph():
    global graph, N, M

    sub1 = [deepcopy(graph[i][:(M//2)]) for i in range(N // 2)]
    sub2 = [deepcopy(graph[i][(M // 2):]) for i in range(N // 2)]
    sub3 = [deepcopy(graph[i][(M // 2):]) for i in range((N // 2), N)]
    sub4 = [deepcopy(graph[i][:(M//2)]) for i in range((N // 2), N)]

    return [sub1, sub2, sub3, sub4]
    
# 1번 연산 : 상하 반전
def solution1():
    global graph, N, M

    graph = graph[::-1]

# 2번 연산 : 좌우 반전
def solution2():
    global graph, N, M
    
    for i in range(N):
        graph[i] = graph[i][::-1]

# 3번 연산 : 시계방향 90도 회전
def solution3():
    global graph, N, M
    
    cp_graph = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            cp_graph[i][j] = graph[(N - 1) - j][i]
    
    graph = cp_graph
    N, M = M, N

# 4번 연산 : 반시계 90도 회전
def solution4():
    global graph, N, M

    cp_graph = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            cp_graph[i][j] = graph[j][(M - 1) - i]

    graph = cp_graph
    N, M = M, N
    

# 5번 연산 : 시계방향 그룹 이동
def solution5():
    global graph, N, M
    
    subGraph = makeSubGraph()

    for i in range(N // 2):
        graph[i] = subGraph[3][i] + subGraph[0][i]
        graph[i + (N // 2)] = subGraph[2][i] + subGraph[1][i]

# 6번 연산 : 반시계방향 그룹 이동
def solution6():
    global graph, N, M

    subGraph = makeSubGraph()

    for i in range(N // 2):
        graph[i] = subGraph[1][i] + subGraph[2][i]
        graph[i + (N // 2)] = subGraph[0][i] + subGraph[3][i]


N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
operator = list(map(int, input().split()))
solutions = [solution1, solution2, solution3, solution4, solution5, solution6]

for type in operator:
    solutions[type - 1]()

for i in range(len(graph)):
    for j in range(len(graph[0])):
        print(graph[i][j], end=' ')
    print()
