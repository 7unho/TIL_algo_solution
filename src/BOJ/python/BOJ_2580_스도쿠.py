# 스도쿠
## 입력값 : 9 * 9의 스도쿠 배열
## 출력값 : 완성된 스도쿠 배열

# 첫번쨰 아이디어, 가로, 세로, 서브배열 탐색하면서 1개인경우 채워나가기
import sys
input = sys.stdin.readline

condition = 45
graph = [list(map(int, input().split())) for _ in range(9)]


# 가로 탐색
for x in range(9):
    sum = 0
    blank_points = list()
    for y in range(9):
        if graph[x][y] == 0:
            blank_points.append([x, y])
            continue
        sum += graph[x][y]
    if len(blank_points) == 1 and sum != condition:
        graph[blank_points[0][0]][blank_points[0][1]] = condition - sum
        
# 세로 탐색

for y in range(9):
    sum = 0
    blank_points = list()
    for x in range(9):
        if graph[x][y] == 0:
            blank_points.append([x, y])
            continue
        sum += graph[x][y]
    if len(blank_points) == 1 and sum != condition:
        graph[blank_points[0][0]][blank_points[0][1]] = condition - sum

# 서브 배열 탐색 ( 3 * 3 )

for dx in range(0, 7, 3):
    for dy in range(0, 7, 3):
        sum = 0
        blank_points = list()
        for x in range(dx, dx + 3):
            for y in range(dy, dy + 3):
                if graph[x][y] == 0:
                    blank_points.append([x, y])
                    continue
                sum += graph[x][y]
            if len(blank_points) == 1 and sum != condition:
                graph[blank_points[0][0]][blank_points[0][1]] = condition - sum
        
for i in range(9):
    for j in range(9):
        print(graph[i][j], end=" ")
    print()
