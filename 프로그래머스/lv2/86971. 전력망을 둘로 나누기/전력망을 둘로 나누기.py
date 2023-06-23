from collections import deque

MAX = 101
visited = []
def init_graph(graph):
    _graph = [[] for _ in range(len(graph) + 3)]
    
    for a, b in graph:
        _graph[a].append(b)
        _graph[b].append(a)
        
    return _graph

def bfs(graph):
    global visited
    answer = []
    for start in range(1, len(graph)):
        q = deque([start])
        cnt = 0
        
        while q:
            node = q.popleft()
            visited[node] = True
            cnt += 1
            
            for next in graph[node]:
                if visited[next]: continue
                visited[next] = True
                q.append(next)
                
        if cnt != 1:
            answer.append(cnt)
            
    return answer

def solution(n, wires):
    global visited
    answer = MAX
    # 간선 하나를 제외한 인접 그래프 생성
    for rm_idx in range(n - 1):
        cpy_wires = wires[:]
        cpy_wires.pop(rm_idx)
        
        graph = init_graph(cpy_wires)
        # # DFS로 노드 개수 구하기
        visited = [False for _ in range(n + 1)]
        
        cnt = bfs(graph)
        
        if len(cnt) == 2:
            answer = min(answer, abs(cnt[0] - cnt[1]))
        
    return answer if answer != MAX else n - 2