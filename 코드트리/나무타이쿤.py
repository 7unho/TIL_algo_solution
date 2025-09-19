"""
n := 격자 크기
m := turn 수
d := 방향
p := 이동거리

초기 영양제 위치
좌측하단 4개

`https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-tycoon/submissions?page=1&page_size=20`

"""
# 우, 우상, 상, 좌상, 좌, 좌하, 하, 우하
dirs = ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1))

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
potion = [(n - 1, 0), (n - 2, 0), (n - 1, 1), (n - 2, 1)]
answer = 0

def outOfRange(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

def move(x, y, d, p):
    """(x, y) -> d방향으로 p만큼 이동"""
    return (n + x + dirs[d][0] * p) % n, (n + y + dirs[d][1] * p) % n
    

def grow_up(x, y):
    count = 0

    for dx, dy in dirs[1::2]:
        nx, ny = x + dx, y + dy

        if outOfRange(nx, ny): continue
        if graph[nx][ny] >= 1:
            count += 1

    graph[x][y] += count

for turn in range(m):
    d, p = map(int, input().split())
    
    for i, (x, y) in enumerate(potion):
    # 1. 포션 이동( d방향으로 p 만큼) 및, 도착좌표 + 1 및
        nx, ny = move(x, y, d - 1, p)
        graph[nx][ny] += 1
        potion[i] = (nx, ny)

    # 2. 인접 대각선 확인 및 성장
    for x, y in potion:
        grow_up(x, y)
    

    nPotion = []
    # 3. potion 제외한 좌표 중 2이상인 애들 2 감소 및 potion에 해당 좌표 추가
    for x in range(n):
        for y in range(n):
            if (x, y) in potion: continue
            if graph[x][y] < 2: continue
            graph[x][y] -= 2
            nPotion.append((x, y))

    potion = nPotion

for i in range(n):
    answer += sum(graph[i])

print(answer)