from collections import deque
# 입력 : M( 사람 ), N ( 그래프 크기 )

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

# N, M 입력부
N, M = map(int, input().split())

# 변수 선언
graph = []
MAX = int(1e9)
visited = [[MAX] * N for _ in range(N)]

base_camp_list = []
targets = []
members = []
res = 0

# 테케 입력
for i in range(N):
    rows = list(map(int, input().split()))
    graph.append(rows)

    if 1 not in rows: continue

    for j in range(len(rows)):
        if rows[j] == 0: continue
        
        base_camp_list.append((i, j))

for _ in range(M):
    x, y = map(int, input().split())
    targets.append((x - 1, y - 1))

# 베이스 캠프 설정
def set_base_camp(targets, base_camp_list):
    for i in range(M):
        dist = MAX
        point = []

        for base_camp in base_camp_list:
            if dist > abs(targets[i][0] - base_camp[0]) + abs(targets[i][1] - base_camp[1]):
                
                dist = abs(targets[i][0] - base_camp[0]) + abs(targets[i][1] - base_camp[1])
                point = [base_camp[0], base_camp[1], i]
        
        members.append(point)
        base_camp_list.remove((point[0], point[1]))

set_base_camp(targets, base_camp_list)

print(members)

def isLongest(before, after, target):
    if abs(before[0] - target[0]) + abs(before[1] - target[1]) - 1 == abs(after[0] - target[0]) + abs(after[1] - target[1]):
        return False
    return True

q = deque([])
for i in range(M):
    q.append([members[i], i + 1])

print(q)
t = 0
res = 0
while q:
    [x, y, member], dist = q.popleft()
    visited[x][y] = member
    graph[x][y] = -1

    res = max(res, dist)

    if targets[member] == (x, y):
        graph[x][y] = -1
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if isLongest((x, y), (nx, ny), targets[member]): continue
        if visited[nx][ny] == member: continue
        if graph[nx][ny] == -1 and visited[nx][ny] < dist: continue
        
        q.append([[nx, ny, member], dist + 1])

print(dist)
