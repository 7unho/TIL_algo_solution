# DFS -> Depth First Search 깊이 우선 탐색
## 노드와 간선으로 이루어진 그래프에서의 인접하다 -> 두 노드가 간선으로 연결되어 있다
### 인접 행렬 ( Adjacency Matrix ) : 2차월 배열로 그래프의 연결 관계를 표현
### 인접 리스트 ( Adjacency List ) : 리스트로 그래프의 연결 관계를 표현

# 5-6.py Adjacency Matrix 방식
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 5-7.py Adjacency List 방식
## Row가 3개인 2차원 리스트로 표현

graph = [[] for _ in range(3)]

# 노드 0에 연결된(인접한) 노드 정보 저장 ( 노드, 거리 )
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)