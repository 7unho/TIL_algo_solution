"""
n := 선수의 수
results = [이기는 선수, 지는 선수]
answer = 순위를 매길 수 있는 선수의 수
"""
def initGraph(n, results):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    for winner, loser in results:
        graph[winner - 1][loser - 1] = 1
        graph[loser - 1][winner - 1] = -1
        
    return graph

def solution(n, results):
    answer = 0
    
    graph = initGraph(n, results)
    
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if a == b: continue
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
                    continue
                if graph[a][k] == -1 and graph[k][b] == -1:
                    graph[a][b] = -1
                    continue
                
    for player in graph:
        if player.count(0) == 1: answer += 1
    return answer