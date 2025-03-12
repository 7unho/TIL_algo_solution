from collections import deque

def solution(info, edges):
    answer = 0
    graph = [set() for _ in range(len(info))]
    for p, c in edges:
        graph[p].add(c)
    
    q = deque([])
    q.append([0, 1, 0, graph[0]])
    
    while q:
        x, sheep, wolf, nNodes = q.popleft()
        
        answer = max(answer, sheep)
        
        for nx in nNodes:
            nSheep = sheep
            nWolf = wolf
            if info[nx] == 1: nWolf += 1
            else: nSheep += 1
            
            if nSheep <= nWolf: continue           

            nDNodes = (nNodes | graph[nx]) - {nx}
            q.append([nx, nSheep, nWolf, nDNodes])
        
    return answer